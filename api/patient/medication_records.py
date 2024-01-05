from db.curd.medication_dao import query_medication_info
from db.curd.patients_medication_records_dao import query_records
from fastapi import Depends
from sqlalchemy.orm import Session
from db.database import get_db
from db.schemas.medication_schema import MedicationSchema
from utils.decorator import *
from utils.token import verify_token


@print_args
@verify_user_effective
def get_medication_history(db: Session = Depends(get_db),
                           current_user: dict = Depends(verify_token)) -> BaseResponse:
    """
    根据患者ID查询药品记录
    """
    patient = current_user.get("patient")
    records = query_records(db, patient.id)
    if len(records) != 0:
        data = [
            {"create_time": r.create_time,
             "medication": MedicationSchema.from_orm(query_medication_info(db, r.medication_id))
             }
            for r in records]

        return BaseResponse(code=200, msg="查询成功", data=data)
    else:
        return BaseResponse(code=200, msg="查询成功", data="暂无开药记录")
