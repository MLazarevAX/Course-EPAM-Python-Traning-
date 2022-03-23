#!/usr/bin/env python


def get_fractions(a_b: str, c_b: str) -> str:
    """
    Create a function what takes two parameters of string type which are fractions and
    returns a sum expression of these fractions and the sum result.
    For example:
    >>> a_b = '1/3'
    >>> c_b = '5/3'
    >>> get_fractions(a_b, c_b)
    '1/3 + 5/3 = 6/3'
    """
    if (isinstance(a_b, str) and (isinstance(c_b, str))
        and len(a_b) > 0 and len(c_b) > 0):
        summer = str(int(a_b.split('/')[0]) + int(c_b.split('/')[0])) +'/'+ a_b.split('/')[1]
        expression = a_b + " + " + c_b + " = " + summer
        return expression
    else:
        raise TypeError("Значения должны быть str и не пустыми")


