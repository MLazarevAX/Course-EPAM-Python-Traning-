# Complete the following code according to the task in README.md.
# Don't change names of classes. Create names for the variables
# exactly the same as in the task.
class SchoolMember:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError('name must be str')
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise ValueError('age must be int')
        self.__age = value

    def show(self):
        return f'Name: {self.name}, Age: {self.age}'


class Teacher(SchoolMember):
    def __init__(self, name: str, age: int, salary: int = None):
        self.name = name
        self.age = age
        self.salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        if not isinstance(value, (int, type(None))):
            raise ValueError('value must be int')
        self.__salary = value

    def show(self):
        if self.salary == None:
            return f'Name: {self.name}, Age: {self.age}'
        return f'Name: {self.name}, Age: {self.age}, Salary: {self.salary}'


class Student(SchoolMember):
    def __init__(self, name: str, age: int, grades: int = None):
        self.name = name
        self.age = age
        self.grades = grades

    @property
    def grades(self):
        return self.__grades

    @grades.setter
    def grades(self, value):
        self.__grades = value

    def show(self):
        if self.grades == None:
            return f'Name: {self.name}, Age: {self.age}'
        return f'Name: {self.name}, Age: {self.age}, Grades: {self.grades}'


if __name__ == "__main__":
    # check if this code is working
    persons = [Teacher("Mr.Snape", 40), Student("Harry", 16, [])]

    for person in persons:
        print(person.show())
