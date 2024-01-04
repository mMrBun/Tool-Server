from sqlalchemy import Column, Integer, String, Date
from db.database import Base


class Patients(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    password = Column(String)
    nickname = Column(String)
    age = Column(Integer)
    date_of_birth = Column(Date)
    gender = Column(String)
    address = Column(String)
    phone_number = Column(String)