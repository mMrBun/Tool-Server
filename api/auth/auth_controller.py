from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm

from utils import TokenResponse, BaseResponse, create_token
from utils.token import verify_token


def login(
        form_data: OAuth2PasswordRequestForm = Depends()
) -> TokenResponse:
    print(form_data.username, form_data.password)
    # TODO: 校验用户名和密码

    # 创建token
    token = create_token({"username": "用户"})
    response = TokenResponse()
    response.access_token = token
    return response


def hello(current_user: dict = Depends(verify_token)):
    """
    测试token鉴权
    """
    print(current_user)
    return BaseResponse(code=200, msg="success", data="hello")
