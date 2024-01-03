from sqlalchemy import Column, Integer, String

from db.database import Base


class UserDao(Base):
    __tablename__ = "test01"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
