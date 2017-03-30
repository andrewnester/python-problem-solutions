import pytest

from problems.streams.find_median import find_median


@pytest.mark.parametrize('test_input, expected', [
    ([5, 4, 3, 2, 1], [5, 4, 4, 3, 3]),
    ([5, 15, 1, 3], [5, 10, 5, 4]),
])
def test_get_sum_of_four(test_input, expected):
    actual = find_median(test_input)
    assert expected == actual
