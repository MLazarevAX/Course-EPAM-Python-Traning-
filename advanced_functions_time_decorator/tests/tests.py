import pytest
from main import func_add as func_test1
from main import execution_time
import time
from typing import Dict, Callable
from .test_func import TIME_100MS, TIME_200MS, TIME_400MS



a = 10,
b = 20,
result = 30,
sleep_time = 0.1


@pytest.mark.parametrize(
        'a, b, result, sleep_time', [
            (10, 20, 30, 0.1),
            (44, 11, 55, 0.2),
            (700, 11, 711, 0.4)
        ]
    )
def test_f1_time_decorator(a, b, result, sleep_time):
    assert result == func_test1(a, b, sleep_time)
    print(execution_time.items(), func_test1.__name__)
    assert execution_time[func_test1.__name__] > sleep_time