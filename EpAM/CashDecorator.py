from functools import wraps

def decorator_with_function_cashing(use_cashe=True, Cash_rez = {}):
    '''
    Декорирующая функция. Принимает в качестве аргуента функцию и кеширует результат, если флаг use_cashe = True.
    :param use_cashe: if True - cash=On, else: Cash=Off.
    :param Cash_rez: Dictionary for cashing inner function and her result
    :return: function result.
    '''
    def decor(func):
        @wraps(func)
        def wrapper(*args, **kwargs):

            if not use_cashe:
                result = func(*args, **kwargs)
                Cash_rez[f'{func.__name__}{args, kwargs}'] = result
                return result
            else:
                try:
                    return Cash_rez[f'{func.__name__}{args}{kwargs}']
                except KeyError:
                    result = func(*args, **kwargs)
                    Cash_rez[f'{func.__name__}{args}{kwargs}'] = result
                    return result
        return wrapper
    return decor

