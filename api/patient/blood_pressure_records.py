from db.curd.blood_pressur_pecords_dao import query_blood_records
from fastapi import Depends
from sqlalchemy.orm import Session
from db.database import get_db
from utils import BaseResponse


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
