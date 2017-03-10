import pytest

from problems.arrays.type_of_array import (get_type_of_array_and_max,
                                           ASCENDING, ASCENDING_ROTATED,
                                           DESCENDING_ROTATED,
                                           DESCENDING)


@pytest.mark.parametrize('test_input, expected', [
    ([1, 2, 3, 4, 5], (5, ASCENDING)),
    ([5, 4, 3, 2, 1], (5, DESCENDING)),
    ([5, 1, 2, 3, 4], (5, ASCENDING_ROTATED)),
    ([1, 5, 4, 3, 2], (5, DESCENDING_ROTATED)),
    ([2, 1, 5, 4, 3], (5, DESCENDING_ROTATED)),
    ([4, 5, 1, 2, 3], (5, ASCENDING_ROTATED)),
])
def test_get_type_of_array_and_max(test_input, expected):
    assert get_type_of_array_and_max(test_input) == expected
