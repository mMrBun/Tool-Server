from sqlalchemy.orm import Session
from db.models.medication import Medication

"""
    药物表操作
"""

skip: int = 0
limit: int = 100


def query_medication_info(db: Session, medication_id: int):
    """
    根据药品信息
    :param db:
    :param patient_id:
    :return:
    """
    return db.query(Medication).filter(Medication.id == medication_id).first()
