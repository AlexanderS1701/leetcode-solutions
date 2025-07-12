from typing import List

class Solution:
    '''
    Дано: список целых чисел nums и целое число target.

    Найди такие два индекса i и j, что:
    nums[i] + nums[j] == target

    Верни их в виде списка из двух элементов [i, j]. Ответ должен содержать индексы найденных чисел.
    Можно считать, что будет ровно одно решение, и нельзя использовать один и тот же элемент дважды.
    Порядок индексов может быть любым ([i, j] или [j, i] — оба верны).
    '''
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in lookup:
                return [lookup[complement], i]
            lookup[num] = i
        return []