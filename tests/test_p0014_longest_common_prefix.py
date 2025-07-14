import pytest
from leetcode_solutions.p0014_longest_common_prefix import Solution


@pytest.mark.parametrize("strs, expected", [
    (["flower", "flow", "flight"], "fl"),
    (["dog", "racecar", "car"], ""),
    (["apple", "applepie", "appletree"], "apple"),
    (["a"], "a"),
    ([""], "")
])
def test_longestCommonPrefix(strs, expected):
    result = Solution.longestCommonPrefix(strs)
    assert result == expected