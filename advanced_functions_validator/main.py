import functools


def validate(low_bound: int, upper_bound: int):
    '''
    low_bound: int = 0,
    upper_bound: int = 256
    '''

    def outer_wrapper(func):
        @functools.wraps(func)
        def inner_wrapper(*args, **kwargs):
            for elem in args:
                if low_bound > elem or elem > upper_bound:
                    return "Function call is not valid!"
            return func(*args, **kwargs)
        return inner_wrapper

    return outer_wrapper


def set_pixel(red: int, green: int, blue: int) -> str:
    """A function for creating a pixel."""
    return "Pixel created!"


