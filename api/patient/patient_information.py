import datetime
from typing import List
from fastapi import UploadFile, File, Form, Depends
from sqlalchemy.orm import Session

from db.database import get_db
from db.schemas.general_employment_inspection_schema import GeneralEmploymentInspectionSchema
from utils import BaseResponse
from db.models.general_employment_inspection import *
from sqlalchemy import and_


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


def get_employment_inspection(db: Session = Depends(get_db)) -> BaseResponse:
    # 获取当前日期
    cur_time = datetime.datetime.now()
    # 计算今天是星期几（0 代表星期一，6 代表星期日）
    weekday = cur_time.weekday()
    # 计算距离下周一的天数（如果今天已经是周一，则返回 0；否则返回负数表示距离下周一还有多少天）
    days_until_next_monday = (0 - weekday) % 7
    # 计算下周一的日期
    next_monday = cur_time + datetime.timedelta(days=days_until_next_monday)
    # 计算下周五的日期
    next_friday = next_monday + datetime.timedelta(days=4)
    inspections = db.query(GeneralEmploymentInspection).filter(
        and_(Column('check_date') >= next_monday.date(), Column('check_date') <= next_friday.date()),
    )
    # 定义一个星期字典
    week_dict = {
        0: "星期一",
        1: "星期二",
        2: "星期三",
        3: "星期四",
        4: "星期五",
        5: "星期六",
        6: "星期日"
    }
    # 根据星期将数据添加到相应的列表中
    result_dict = {}
    for inspection in inspections:
        obj = GeneralEmploymentInspectionSchema(**inspection.__dict__)
        week_day = obj.check_date.weekday()
        if week_day not in result_dict:
            result_dict[week_dict[week_day]] = 0
        result_dict[week_dict[week_day]] += 1
    return BaseResponse(code=200, msg="文件上传与向量化完成",
                        data=result_dict)
