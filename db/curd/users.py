from sqlalchemy.orm import Session
from db.models import userDao
# from db.schemas import userSchema


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(userDao.UserDao).offset(skip).limit(limit).all()
