import pytest

from problems.strings.rearrange_characters import is_possible_to_rearrange


@pytest.mark.parametrize('test_input, expected', [
    ('aabbcc', True),
    ('geeksforgeeks', True),
    ('bbbabaaacd', True),
    ('bbbbb', False),
    ('aaaaaabbcc', False),
])
def test_is_possible_to_rearrange(test_input, expected):
    assert is_possible_to_rearrange(test_input) == expected
