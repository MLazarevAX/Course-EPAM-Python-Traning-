#!/usr/bin/env python
from typing import Callable, Iterable


def apply(func: Callable):
    """
    Create a decorators factory (decorator itself).
    The factory accepts a function (lambda) as an input and returns a decorator
    that will return the result of the function as the first argument,
    the result of the decorated function is passed.
    The function which the factory accepts (in
    the example below it is a `lambda`)
    can take one positional parameter only.


    For example:

    @apply(lambda user_id: user_id + 1)
    def return_user_id():
        return 42

    >>> return_user_id()
    43
    """
    def inner(function_inner: Callable):
        def finish(*args, **kwargs):
            return func(function_inner(*args, **kwargs))
        return finish
    return inner


def return_user_id():
    return 42

decor = apply(lambda user_id: user_id + 1)(return_user_id)

print(decor())

class My_Iterator:
    def __init__(self, iter_obj: Iterable):
        self.iter_obj = iter_obj

    def __next__(self):
        if self.iter_obj:
            value = self.iter_obj[0]
            self.iter_obj = self.iter_obj[1:]
            return value
        else:
            raise StopIteration

    def __iter__(self):
        return self