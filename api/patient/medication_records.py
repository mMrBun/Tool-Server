from db.curd.medication_dao import query_medication_info
from db.curd.patients_medication_records_dao import query_records
from fastapi import Depends
from sqlalchemy.orm import Session
from db.database import get_db
from utils import BaseResponse
from utils.token import verify_token


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
