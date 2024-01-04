from sqlalchemy.orm import Session
from db.models.sys_user_model import sys_user


def find_sys_user_by_username(db: Session, username: str) -> sys_user:
    return db.query(sys_user).filter(sys_user.username == username).first()
