from sqlalchemy.orm import Session
from db.models.patients_medication_records import PatientsMedicationRecordsModel


def query_records(db: Session, patient_id: int):
    """
    根据用户ID查询药品记录
    :param db:
    :param patient_id:
    :return:
    """
    return db.query(PatientsMedicationRecordsModel).filter(
        patient_id == PatientsMedicationRecordsModel.patients_id).all()
