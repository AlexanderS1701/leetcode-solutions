class Solution:
    '''
    Given an integer x, return true if x is a palindrome, and false otherwise.
    '''
    @staticmethod
    def isPalindrome(x: int) -> bool:
        return str(x) == str(x)[::-1]

