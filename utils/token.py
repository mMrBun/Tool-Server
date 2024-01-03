from datetime import datetime, timedelta
from typing import Union
import jwt

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
