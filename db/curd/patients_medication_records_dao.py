from sqlalchemy.orm import Session
from db.models.patients_medication_records import PatientsMedicationRecords




def query_records(db: Session, patient_id: int):
    """
    根据用户ID查询药品记录
    :param db:
    :param patient_id:
    :return:
    """
    return db.query(PatientsMedicationRecords).filter(patient_id == PatientsMedicationRecords.patients_id).all()

