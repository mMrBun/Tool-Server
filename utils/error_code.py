from enum import Enum


class ErrorCode(Enum):
    INSERT_ERROR = (100001, "新增数据出错，请查看日志ERROR")

    def __init__(self, code, msg):
        self.code = code
        self.msg = msg
