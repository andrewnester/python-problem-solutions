import pytest

from problems.arrays.xor_game import get_xor_value


@pytest.mark.parametrize('test_input, expected', [
    ([1, 2, 3], 2),
    ([1, 2, 3, 4], 0),
    ([33, 52, 38, 29, 76, 8, 75, 22, 59, 96, 30, 38, 36, 94, 19, 29, 44], 62),
])
def test_get_xor_value(test_input, expected):
    assert get_xor_value(test_input) == expected
