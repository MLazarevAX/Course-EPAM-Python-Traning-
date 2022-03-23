import time
from typing import Dict, Callable
from functools import wraps

execution_time: Dict[str, float] = {}


def time_decorator(func: Callable) -> Dict[str, float]:
    """
    Create a decorator function `time_decorator`
    which has to calculate decorated function execution time
    and put this time value to `execution_time` dictionary where `key` is
    decorated function name and `value` is this function execution time.
    """
    @wraps(func)
    def wrapper_func(*args, **kwargs):
        global execution_time
        start_time_func = time.time()
        result = func(*args, **kwargs)
        end_time_func = time.time() - start_time_func
        execution_time[func.__name__] = end_time_func
        return result
    return wrapper_func

@time_decorator
def func_add(a, b, sleep_time):
    time.sleep(sleep_time)
    return a + b

