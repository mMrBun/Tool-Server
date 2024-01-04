from sqlalchemy import Column, Integer, String, Date
from db.database import Base


class MedicationRecords(Base):
    __tablename__ = "medication_records"

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer)
    medication_name = Column(String)
    prescribed_date = Column(Date)
    dosage = Column(String)
    frequency = Column(String)
    is_delete = Column(Integer)
