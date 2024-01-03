from sqlalchemy import Column, Integer, String, Date
from db.database import Base


class Patient(Base):
    __tablename__ = "health_check_records"

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer)
    check_date = Column(Date)
    status = Column(String)
    result_summary = Column(String)
