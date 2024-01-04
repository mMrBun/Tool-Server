from typing import List
from fastapi import UploadFile, File, Form, Depends
from sqlalchemy.orm import Session
from db.curd.users import get_users, add_user
from db.curd.medication_dao import query_medication_info
from db.curd.patients_medication_records_dao import query_records
from db.curd.blood_pressur_pecords_dao import query_blood_all_records, query_blood_records
from db.database import get_db
from db.schemas.patients_schema import PatientsSchema
from utils import BaseResponse
from utils.error_code import ErrorCode
from utils.token import verify_token


def upload_docs(
        files: List[UploadFile] = File(..., description="上传文件，支持多文件"),
        knowledge_base_name: str = Form(..., description="知识库名称", examples=["samples"]),
        override: bool = Form(False, description="覆盖已有文件"),
        to_vector_store: bool = Form(True, description="上传文件后是否进行向量化"),
        chunk_size: int = Form(500, description="知识库中单段文本最大长度"),
        chunk_overlap: int = Form(50, description="知识库中相邻文本重合长度"),
        zh_title_enhance: bool = Form(True, description="是否开启中文标题加强"),
        not_refresh_vs_cache: bool = Form(False, description="暂不保存向量库（用于FAISS）"),
) -> BaseResponse:
    """
    API接口：上传文件，并/或向量化
    """
    print(
        files,
        knowledge_base_name,
        override,
        to_vector_store,
        chunk_size,
        chunk_overlap,
        zh_title_enhance,
        not_refresh_vs_cache
    )

    return BaseResponse(code=200, msg="文件上传与向量化完成", data={"failed_files": "xxx"})


def get_medication_history(patientId: int, db: Session = Depends(get_db),
                           current_user: dict = Depends(verify_token)) -> BaseResponse:
    """
    根据患者ID查询药品记录
    :param patientId:患者ID
    :param current_user:鉴权
    :param db:
    """
    records = query_records(db, patientId)
    if len(records) != 0:
        data = [
            {"create_time": r.create_time,
             "medication":
                 {"name": query_medication_info(db, r.medication_id).medication_name,
                  "dosage": query_medication_info(db, r.medication_id).dosage,
                  "frequency": query_medication_info(db, r.medication_id).frequency
                  }
             }
            for r in records]
        return BaseResponse(code=200, msg="查询成功", data=data)
    else:
        return BaseResponse(code=200, msg="查询成功", data="暂无开药记录")


def db_query(db: Session = Depends(get_db)) -> BaseResponse:
    """
        API接口： 数据库查询
    """
    objs = get_users(db)
    return BaseResponse(code=200, msg="查询数据库成功",
                        data=[{"id": obj.id, "name": obj.name, "age": obj.age} for obj in objs])


def get_blood_pressureHistory(patientId: int, start_time: str = None, end_time: str = None,
                              db: Session = Depends(get_db)):
    """
    查询历史血压记录
    :param end_time:
    :param start_time:
    :param patientId:
    :param db:
    :return:
    """

    records = query_blood_records(db, patientId, start_time, end_time)
    if len(records) != 0:
        data = [
            {"measure_time": r.create_time,
             "systolic_pressure": r.systolic_pressure,
             "diastolic_pressure": r.diastolic_pressure,
             }
            for r in records]
        return BaseResponse(code=200, msg="查询成功", data=data)
    return BaseResponse(code=200, msg="查询成功", data="近期并未测量血压。")


def sign_in(
        db: Session = Depends(get_db),
        patient: PatientsSchema = Form(..., description="患者信息")
):
    if add_user(db, patient):
        return BaseResponse(code=200, msg="success", data=[])
    else:
        return BaseResponse(code=ErrorCode.INSERT_ERROR.code, msg=ErrorCode.INSERT_ERROR.msg, data=[])
