from fastapi import Body
from db.curd.users import add_user
from db.schemas.patients_schema import PatientsSchema
from utils.error_code import ErrorCode
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from db.curd.patients_dao import query_patients_by_username
from db.database import get_db
from utils import BaseResponse, create_token
from utils.token import verify_password


def register(
        db: Session = Depends(get_db),
        patient: PatientsSchema = Body(..., description="患者信息")
):
    if add_user(db, patient):
        return BaseResponse(code=200, msg="success", data=[])
    else:
        return BaseResponse(code=ErrorCode.INSERT_ERROR.code, msg=ErrorCode.INSERT_ERROR.msg, data=[])


def login(
        form_data: OAuth2PasswordRequestForm = Depends(),
        db: Session = Depends(get_db)
) -> BaseResponse:
    username = form_data.username
    password = form_data.password
    patient = query_patients_by_username(db, username)

    if patient is None or not verify_password(password, patient.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    # 创建token
    token = create_token({"sub": username})

    return BaseResponse(code=200, msg="success", data=token)
