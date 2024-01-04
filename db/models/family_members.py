from sqlalchemy import Column, Integer, String
from db.database import Base


class FamilyMembers(Base):
    __tablename__ = "family_members"

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer)
    name = Column(String)
    relation = Column(String)
    contact_number = Column(String)