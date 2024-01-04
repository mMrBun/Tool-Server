from sqlalchemy.orm import Session
from db.models.sys_user import SysUser


def find_sys_user_by_username(db: Session, username: str) -> SysUser:
    return db.query(SysUser).filter(SysUser.username == username).first()
