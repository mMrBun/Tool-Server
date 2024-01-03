from utils import BaseResponse, create_token
from fastapi import Form


def login(
        username: str = Form(..., description="用户名"),
        password: str = Form(..., description="密码")
) -> BaseResponse:
    """
    user login logic.
    :param username:
    :param password:
    :return: JWT token string.
    """
    print(username,password)
    # TODO: 校验用户名和密码

    # 创建token
    token = create_token({"username": "用户"})

    response = BaseResponse()
    response.data = token
    return response
