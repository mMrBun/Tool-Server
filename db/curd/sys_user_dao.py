from sqlalchemy.orm import Session
from db.models.patients import Patients


def find_sys_user_by_username(db: Session, username: str) -> Patients:
    # return db.query(Patients).filter(Patients.username == username).first()
    return db.query(Patients).filter(Patients.username == username).first()
