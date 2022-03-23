from typing import Callable
import functools


def deanon(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func.__name__, func(*args, **kwargs)

    return wrapper


