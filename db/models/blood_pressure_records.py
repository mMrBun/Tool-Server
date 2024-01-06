from sqlalchemy import Column, Integer, String, Date
from db.database import Base


class BloodPressureRecordsModel(Base):
    __tablename__ = "blood_pressure_records"

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer)
    systolic_pressure = Column(Integer)
    diastolic_pressure = Column(Integer)
    create_time = Column(Date)
