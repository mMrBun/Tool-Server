from db.curd.blood_pressur_pecords_dao import query_blood_records
from fastapi import Depends
from sqlalchemy.orm import Session
from db.database import get_db
from utils.decorator import *
from utils.token import verify_token
from db.schemas.blood_pressure_records_schema import BloodPressureRecordsSchema


@print_args
@verify_user_effective
def get_blood_pressureHistory(start_time: str = None, end_time: str = None,
                              db: Session = Depends(get_db),
                              current_user: dict = Depends(verify_token)):
    """
    查询历史血压记录
    """
    patient = current_user.get("patient")
    records = query_blood_records(db, patient.id, start_time, end_time)
    if len(records) != 0:
        data = [
            BloodPressureRecordsSchema.from_orm(r)
            for r in records]
        return BaseResponse(code=200, msg="查询成功", data=data)
    return BaseResponse(code=200, msg="查询成功", data="暂无测量数据。")
