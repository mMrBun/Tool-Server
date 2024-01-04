from sqlalchemy.orm import Session

from db.models.vaccination import Vaccination


def get_vaccinations_for_patient(db: Session, patient_id: int):
    return db.query(Vaccination).filter_by(patient_id=patient_id).all()
