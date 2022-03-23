import pytest
from main import Field



value = []


@pytest.mark.parametrize(
    "value", [[], "test", 0, dict(), None]
)
def test_class_encapsulation(value):
    field = Field()
    field.set_value(value)
    assert field.get_value() == value