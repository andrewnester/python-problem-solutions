import pytest

from problems.strings.rotated_by_two import is_rotated_by_two


@pytest.mark.parametrize('a, b, expected', [
    ('amazon', 'azonam', 1),
    ('amazon', 'onamaz', 1),
    ('geeksforgeeks', 'geeksgeeksfor', 0),
])
def test_rotated_by_two(a, b, expected):
    assert is_rotated_by_two(a, b) == expected
