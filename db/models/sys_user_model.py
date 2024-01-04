from sqlalchemy import Column, BIGINT, VARCHAR, Integer
from db.database import Base


class sys_user(Base):
    __tablename__ = "sys_user"

    id = Column(BIGINT, primary_key=True, index=True)
    username: str = Column(VARCHAR)
    password: str = Column(VARCHAR)
    nickname: str = Column(VARCHAR)
    age: int = Column(Integer)
    gender: str = Column(VARCHAR)
