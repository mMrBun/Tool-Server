import functools
import logging


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
