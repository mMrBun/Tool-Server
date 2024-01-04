from enum import Enum


class ErrorCode(Enum):
    INSERT_ERROR = (100001, "新增数据出错，请查看日志ERROR")
    TOKEN_INVALID_ERROR = (401, "Token失效，请重新登录")
    USERNAME_OR_PASSWORD_ERROR = (100002, "用户名或密码错误")
    USER_NOT_FOUND_ERROR = (100003, "用户不存在，请检查账号或密码")
    UNKNOWN_ERROR = (100004, "未知异常：")

    def __init__(self, code, msg):
        self.code = code
        self.msg = msg
