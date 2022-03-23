import pytest

from main import intersect

result = set()
parameters = (('S', 'A', 'C'), ('P', 'C'), ('G', 'H'))


@pytest.mark.parametrize(
    'result, parameters', [
        ({'S', 'A', 'M'}, (['S', 'A', 'M'], ['S', 'P', 'A', 'M', 'C'])),
        ({'S'}, (['S', 'A'], ['S', 'P', 'C'])),
        (set(), (('S', 'A'), ('P', 'C'), ('G', 'H'))),
        (set(), (('S', 'A', 'C'), ('P', 'C'), ('G', 'H'))),
        ({'S', 'C'}, (('S', 'A', 'C'), ('P', 'C', 'S'), ('G', 'H', 'S', 'C'))),
    ]
)
def test_intersect(result, parameters):
    assert result == intersect(*parameters)
