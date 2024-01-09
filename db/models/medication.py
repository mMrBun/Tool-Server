from sqlalchemy import Column, Integer, String, Date, text
from db.database import Base


class Medication(Base):
    __tablename__ = "medication"

    id = Column(Integer, primary_key=True, index=True)
    medication_name = Column(String)
    dosage = Column(String)
    frequency = Column(String)
    role = Column(String)
    taboo_information = Column(String)
