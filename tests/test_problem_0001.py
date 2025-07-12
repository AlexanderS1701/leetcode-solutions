import pytest
from leetcode_solutions.problem_0001 import Solution

@pytest.mark.parametrize("nums, target, expected", [
    ([2, 7, 11, 15], 9, [0, 1]),
    ([3, 2, 4], 6, [1, 2]),
    ([3, 3], 6, [0, 1]),
])
def test_two_sum(nums, target, expected):
    result = Solution().two_sum(nums, target)
    assert result == expected or result == expected[::-1]