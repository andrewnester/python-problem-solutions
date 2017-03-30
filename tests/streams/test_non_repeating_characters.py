import pytest

from problems.streams.non_repeating_characters import get_non_repeating_characters


@pytest.mark.parametrize('test_input, expected', [
    (['a', 'a', 'b', 'c'], ['a', '-1', 'b', 'b']),
    (['a', 'a', 'b', 'c', 'b'], ['a', '-1', 'b', 'b', 'c']),
    (['a', 'b', 'c', 'c', 'a', 'b', 'a'], ['a', 'a', 'a', 'a', 'b', '-1', '-1']),
    (['w', 'l', 'r', 'b', 'b', 'm', 'q', 'b', 'h', 'c', 'd', 'a', 'r', 'z', 'o', 'w', 'k', 'k', 'y'], ['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'l', 'l', 'l', 'l']),
])
def test_get_sum_of_four(test_input, expected):
    actual = get_non_repeating_characters(test_input)

    assert len(expected) == len(actual)

    for v in actual:
        assert v in expected
