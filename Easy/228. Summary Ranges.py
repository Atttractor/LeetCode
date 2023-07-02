"""
Easy
You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of
nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not
in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b

Runtime: 42.78% 47ms
Memory: 26.14% 16.5MB
"""
from typing import List


class Solution:
    @staticmethod
    def summaryRanges(nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [str(nums[0])]

        start, cur, end = nums[0], 1, nums[0]
        res = []

        while cur < len(nums):
            if nums[cur] - nums[cur - 1] == 1:
                end = nums[cur]
                cur += 1
                if cur == len(nums):
                    res.append(f'{start}->{end}')
            else:
                if start == end:
                    res.append(str(start))
                else:
                    res.append(f'{start}->{end}')
                start, end = nums[cur], nums[cur]
                cur += 1
                if start == nums[-1]:
                    res.append(str(start))

        return res


if __name__ == '__main__':
    Solution.summaryRanges([0, 2, 3, 4, 6, 8, 9])
    Solution.summaryRanges([0, 1, 2, 4, 5, 7])
