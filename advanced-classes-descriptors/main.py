class PriceControl:
    """
    Descriptor which don't allow to set price
    less than 0 and more than 100 included.
    """

    def __init__(self, name):
        self.name = name

    def __getattr__(self, instance):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if value > 100 or value < 0:
            raise ValueError('Price must be between 0 and 100.')
        instance.__dict__[self.name] = value




class NameControl:
    """
    Descriptor which don't allow to change field value after initialization.
    """

    def __init__(self, name):
        self.name = name
        self.__value = None

    def __getattr__(self, instance):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if self.__value is not None:
            raise ValueError(f"{self.name.title()} can not be changed.")
        instance.__dict__[self.name] = value
        self.__value = value


class Book:
    author = NameControl(name="author")
    name = NameControl(name="name")
    price = PriceControl(name="price")

    def __init__(self, author, name, price):
        self.author = author
        self.name = name
        self.price = price


