from sqlalchemy import Column, Integer, String, Date, ForeignKey, BIGINT
from db.database import Base


class Vaccination(Base):
    __tablename__ = 'vaccination'

    vaccination_id = Column(BIGINT, primary_key=True, index=True)
    patient_id = Column(BIGINT)
    vaccine_name = Column(String(50))
    vaccination_date = Column(Date)
    vaccination_location = Column(String(100))
    vaccination_provider = Column(String(100))
