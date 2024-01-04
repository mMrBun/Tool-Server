from sqlalchemy.orm import Session
from db.models import patients
from db.schemas.patients_schema import PatientsSchema
from utils.token import hash_password


# from db.schemas import user_schema


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(patients.Patients).offset(skip).limit(limit).all()


def add_user(db: Session, patients_schema: PatientsSchema):
    try:
        patient_data = patients_schema.dict()
        patient_data['password'] = hash_password(patient_data['password'])
        patient = patients.Patients(**patient_data)
        db.add(patient)
        db.commit()
        return True
    except Exception as e:
        print(e)
        return False
