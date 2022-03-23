class Field:
    def __init__(self):
        pass

    # TODO: add your code here
    def get_value(self):
        return self.__value

    def set_value(self, value):
        self.__value = value




if __name__ == "__main__":
    # Check if this code is working
    field = Field()
    field.set_value(123)
    print(field.get_value())
