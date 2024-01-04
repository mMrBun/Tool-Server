from sqlalchemy import Column, Integer, String, Date
from db.database import Base


class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    date_of_birth = Column(Date)
    gender = Column(String)
    address = Column(String)
    phone_number = Column(String)