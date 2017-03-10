import pytest

from problems.strings.longest_palindrome_substring import longest_palindrome_substring


@pytest.mark.parametrize('test_input, expected', [
    ('aaabbaba', 'abba'),
    ('owo', 'owo'),
    ('a', 'a'),
    ('aa', 'aa'),
    ('abcddef', 'dd'),
    ('ababababab', 'ababababa'),
    ('asdfwqdadasaasdvcaaqqd', 'saas'),
])
def test_longest_palindrome_substring(test_input, expected):
    assert longest_palindrome_substring(test_input) == expected
