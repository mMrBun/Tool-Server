from sqlalchemy.orm import Session
from db.models.blood_pressure_records import BloodPressureRecords
from datetime import date

"""
    血压记录表操作
"""

skip: int = 0,
limit: int = 100


def query_blood_all_records(db: Session):
    """
    根据查询过往的所有血压值数据
    :param db:
    :param patient_id:
    :return:
    """
    return db.query(BloodPressureRecords).all()


def query_blood_records(db: Session, patient_id: int, start_time: date, end_time: date):
    """
    查询时间间隔之内的血压记录
    :param db:
    :param patient_id:
    :param start_time:
    :param end_time:
    :return:
    """
    if start_time is None:
        start_time = date.min
    if end_time is None:
        end_time = date.max
    return db.query(BloodPressureRecords).filter(patient_id == BloodPressureRecords.patient_id,
                                                 BloodPressureRecords.create_time > start_time,
                                                 BloodPressureRecords.create_time < end_time).all()
