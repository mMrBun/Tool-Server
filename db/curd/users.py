from sqlalchemy.orm import Session
from db.models import user_dao


# from db.schemas import user_schema


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(user_dao.UserDao).offset(skip).limit(limit).all()


def add_user(db: Session):
    user = user_dao.UserDao(name="zmq", age=24, id=4)
    db.add(user)
    db.commit()
