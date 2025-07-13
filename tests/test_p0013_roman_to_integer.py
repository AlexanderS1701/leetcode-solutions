import pytest
from leetcode_solutions.p0013_roman_to_integer import Solution


@pytest.mark.parametrize("s, expected", [
    ('III', 3),
    ('LVIII', 58),
    ('MCMXCIV', 1994)
])
def test_romanToInt(s, expected):
    result = Solution.romanToInt(s)
    assert result == expected
