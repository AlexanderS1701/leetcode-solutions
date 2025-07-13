import pytest
from leetcode_solutions.p0001_two_sum import Solution


@pytest.mark.parametrize("nums, target, expected", [
    ([2, 7, 11, 15], 9, [0, 1]),
    ([3, 2, 4], 6, [1, 2]),
    ([3, 3], 6, [0, 1]),
])
def test_twoSum(nums, target, expected):
    result = Solution.twoSum(nums, target)
    assert result == expected or result == expected[::-1]
