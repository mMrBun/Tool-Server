from sqlalchemy.orm import Session
from db.models.patients import Patients

"""
    病人表操作
"""

skip: int = 0
limit: int = 100


def query_patients_all_info(db: Session):
    """
    查询所有的患者信息
    :param db:
    :return:
    """
    return db.query(Patients).offset(skip).limit(limit).all()


def query_patients_info_by_id(db: Session, patient_id: int) -> Patients:
    """
    根据ID查询单个患者的信息
    :param db:
    :param patient_id:
    :return:
    """
    return db.query(Patients).filter(Patients.id == patient_id).first()
