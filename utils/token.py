from datetime import datetime, timedelta
from typing import Union
import jwt
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from sqlalchemy.orm import Session

from db.curd.sys_user_dao import find_sys_user_by_username
import db.database

SECRET_KEY = "tool-server"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_token(data: dict) -> str:
    """
    Create a JWT token with the provided data.
    :param data: Data to be included in the token payload.
    :return: JWT token string.
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(payload=to_encode, key=SECRET_KEY, algorithm=ALGORITHM)


def decode_token(token: str) -> Union[dict, None]:
    """
    Decode a JWT token
    :param token: JWT token string.
    :return: Decoded token payload or Node if decoding fails.
    """
    try:
        payload = jwt.decode(jwt=token, key=SECRET_KEY, algorithms=ALGORITHM)
        return payload
    except jwt.ExpiredSignatureError:
        # Token has expired
        return None
    except jwt.InvalidTokenError:
        # Invalid token
        return None


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/login")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_token(token: str = Depends(oauth2_scheme), db: Session = Depends(db.database.get_db)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Invalid credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = decode_token(token)
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        patient = find_sys_user_by_username(db, username)
        payload.update({"patient": patient})
    except EOFError:
        raise credentials_exception
    return payload


# 验证密码
def verify_password(plain_password, hashed_password):
    result = pwd_context.verify(plain_password, hashed_password)
    return result


def hash_password(plain_password):
    return pwd_context.hash(plain_password)

