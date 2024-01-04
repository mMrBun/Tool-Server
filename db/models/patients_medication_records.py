from db.database import Base
from sqlalchemy import Column, Integer, DATETIME


class PatientsMedicationRecords(Base):
    __tablename__ = "patients_medication_records"

    id = Column(Integer, primary_key=True, index=True)
    patients_id = Column(Integer)
    medication_id = Column(Integer)
    create_time = Column(DATETIME)
