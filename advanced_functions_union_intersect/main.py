def union(*args) -> set:
    return {elem for arg in args for elem in arg}


def intersect(*args) -> set:
    first_arg, *second_arg = args
    if first_arg:
        for arg in second_arg:
            first_arg = set(first_arg).intersection(set(arg))
        return first_arg
    return set()


