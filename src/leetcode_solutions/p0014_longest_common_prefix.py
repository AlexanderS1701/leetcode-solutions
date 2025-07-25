from typing import List

class Solution:
    '''
    Write a function to find the longest common prefix string amongst an array of strings.
    If there is no common prefix, return an empty string "".
    '''
    @staticmethod
    def longestCommonPrefix(strs: List[str]) -> str:
        if not strs:
            return ""

        prefix = strs[0]

        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix