import pytest
from main import *

low_bound: int = 0
upper_bound: int = 256
result = 'Pixel created!'
ERROR_MESSAGE = "Function call is not valid!"
SUCCES_MESSAGE = 'Pixel created!'

@pytest.mark.parametrize(
        'result, red, green, blue', [
            (SUCCES_MESSAGE, 0, 0, 0),
            (SUCCES_MESSAGE, 256, 256, 256),
            (SUCCES_MESSAGE, 255, 255, 255),
            (SUCCES_MESSAGE, 255, 0, 255),
            (ERROR_MESSAGE, 256, 256, 257),
            (ERROR_MESSAGE, -256, 70, 257)
        ]
    )
def test_validate_decorator(result, red, green, blue):
    @validate(low_bound, upper_bound)
    def decorated_function(red: int, green: int, blue: int) -> str:
        """A function for creating a pixel."""
        return "Pixel created!"

    assert result == decorated_function(red, green, blue)
