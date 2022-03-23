import pytest
from main import *


name = 'Henry'
age = 14
grades = [5, 3, 5, 2, 3, 4, ...]
expected = 'Name: Henry, Age: 14, Grades: [5, 3, 5, 2, 3, 4, 5]'


@pytest.mark.parametrize(
    "name,age,grades,expected", [
        ("Sam S.", 10, 5, "Name: Sam S., Age: 10, Grades: 5"),
        (
            "Henry", 14, [5, 3, 5, 2, 3, 4, 5],
            "Name: Henry, Age: 14, Grades: [5, 3, 5, 2, 3, 4, 5]"
        ),
        (
            "Penny", 17, {"Math": 5, "PE": 3},
            "Name: Penny, Age: 17, Grades: {'Math': 5, 'PE': 3}"
        )
    ]
)
def test_student_show(name, age, grades, expected):
    student_obj = Student(name=name, age=age, grades=grades)
    expected == student_obj

def test_parent_show_method():
    assert 'show' in SchoolMember.__dict__