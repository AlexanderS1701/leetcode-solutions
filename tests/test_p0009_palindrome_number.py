import pytest
from leetcode_solutions.p0009_palindrome_number import Solution


@pytest.mark.parametrize("x, expected", [
    (121, True),
    (-121, False),
    (10, False)
])
def test_isPalindrome(x, expected):
    result = Solution.isPalindrome(x)
    assert result == expected
