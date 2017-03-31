import pytest

from problems.arrays.stack_sort import stack_sort


@pytest.mark.parametrize('test_input, expected', [
    ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
    ([3, 1, 5, 2, 4], [5, 4, 3, 2, 1]),
    ([5, 4, 3, 2, 1], [5, 4, 3, 2, 1]),
    ([5, 3, 5, 4, 1], [5, 5, 4, 3, 1]),
])
def test_stack_sort(test_input, expected):
    assert stack_sort(test_input) == expected
