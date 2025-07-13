
class Solution:
    '''
    Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
    Given a roman numeral, convert it to an integer.
    '''
    @staticmethod
    def romanToInt(s: str) -> int:
        values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        total = 0
        prev_value = 0

        for char in reversed(s):
            current = values[char]
            if current < prev_value:
                total -= current
            else:
                total += current
                prev_value = current

        return total
