from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from db.curd.sys_user_dao import find_sys_user_by_username
from db.database import get_db
from utils import TokenResponse, BaseResponse, create_token
from utils.token import verify_token


def login(
        form_data: OAuth2PasswordRequestForm = Depends(),
        db: Session = Depends(get_db)
) -> TokenResponse:
    """
    User login
    :param form_data: OAuth2PasswordRequestForm Object
    :param db:  DB Session
    :return:
    """
    username = form_data.username
    password = form_data.password
    sys_user = find_sys_user_by_username(db, username)

    if sys_user is None or sys_user.password != password:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    # create token
    token = create_token({"sub": username})
    response = TokenResponse()
    response.access_token = token
    return response


def hello(current_user: dict = Depends(verify_token)):
    """
    Test token Authentication
    """

    sys_user = current_user.get("sys_user")

    print(sys_user.username, sys_user.password)
    return BaseResponse(code=200, msg="success", data="hello")
