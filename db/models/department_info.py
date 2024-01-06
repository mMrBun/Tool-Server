from sqlalchemy import Column, Integer, String, Date, Text
from db.database import Base


class DepartmentInfoModel(Base):
    __tablename__ = "department_info"

    department_id = Column(Integer, primary_key=True, index=True)
    department_name = Column(String)
    department_phone = Column(String)
    location = Column(String)
    lead_physicians = Column(String)
    clinic_start_hours = Column(String)
    clinic_end_hours = Column(String)
    patient_guide = Column(Text)
    corresponding_symptom = Column(String)
