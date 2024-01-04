import functools
import logging

from utils import BaseResponse


def print_args(func):
    """
    打印函数入参装饰器
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        logging.info(f"调用 {func.__name__}({signature})")
        return func(*args, **kwargs)

    return wrapper


def verify_user_effective(f):
    """
    Token验证装饰器
    """
    @functools.wraps(f)
    def decorated_function(*args, **kwargs):
        current_user = kwargs.get('current_user') or args[0].current_user
        if current_user.get("code") != 200:
            return BaseResponse(code=current_user.get("code"), msg=current_user.get("msg"), data=current_user.get("data"))
        return f(*args, **kwargs)
    return decorated_function
