from sqlalchemy.orm import Session
from db.models.blood_pressure_records import BloodPressureRecordsModel
from datetime import date

"""
    血压记录表操作
"""

skip: int = 0,
limit: int = 100


def query_blood_all_records(db: Session):
    """
    根据查询过往的所有血压值数据
    """
    return db.query(BloodPressureRecordsModel).all()


def query_blood_records(db: Session, patient_id: int, start_time: date, end_time: date):
    """
    查询时间间隔之内的血压记录
    """
    if start_time is None:
        start_time = date.min
    if end_time is None:
        end_time = date.max
    return db.query(BloodPressureRecordsModel).filter(patient_id == BloodPressureRecordsModel.patient_id,
                                                      BloodPressureRecordsModel.create_time > start_time,
                                                      BloodPressureRecordsModel.create_time < end_time).all()
