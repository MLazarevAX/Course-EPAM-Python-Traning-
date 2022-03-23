from typing import Union, Callable
NumType = Union[int, float]

def some_expression_with_rounding(a: NumType, b: NumType) -> NumType:
    result = (12 * a + 25 * b) / (1 + a**(2**b))
    return round(result, 2)

def time_decorator(func: Callable):

    execution_time = {}
    def wrapper(*args, **kwargs):
        start_time_func = time.time()
        func(*args, **kwargs)
        end_time_func = time.time() - start_time_func
        execution_time[func.__name__] = end_time_func
        return execution_time
    return wrapper




