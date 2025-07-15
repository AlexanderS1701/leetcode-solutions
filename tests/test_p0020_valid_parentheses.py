import pytest
from leetcode_solutions.p0020_valid_parentheses import Solution


@pytest.mark.parametrize("s, expected", [
    ("()", True),
    ("()[]{}", True),
    ("()", True),
    ("", True),
    ("(([]){})", True),
    ("(]", False),
    ("}{", False),
    ("{", False),
    ("]", False),
    ("Жопа", False),
])
def test_isValid(s, expected):
    result = Solution.isValid(s)
    assert result == expected