import pytest

from problems.arrays.sum_of_four import get_sum_of_four


@pytest.mark.parametrize('test_input, desire, expected', [
    ([1, 2, 3, 4, 5], 10, [(1, 2, 3, 4)]),
    ([2, 3, 4, 5, 9, 7, 8], 23, [(2, 4, 9, 8), (3, 5, 7, 8), (2, 5, 9, 7), (3, 4, 9, 7)]),
])
def test_get_sum_of_four(test_input, desire, expected):
    actual = get_sum_of_four(test_input, desire)
    assert len(expected) == len(actual)

    for v in actual:
        assert v in expected
