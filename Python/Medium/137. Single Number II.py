"""
Medium

Given an integer array nums where every element appears three times except for one, which appears exactly once. Find
the single element and return it.

You must implement a solution with a linear runtime complexity and use only constant extra space.

Runtime: 81.56% 71ms
Memory: 6.77% 18.7MB
"""
from collections import Counter
from typing import List


class Solution:
    @staticmethod
    def singleNumber(nums: List[int]) -> int:
        return Counter(nums).most_common()[-1][0]


if __name__ == '__main__':
    Solution.singleNumber([0, 1, 0, 1, 0, 1, 99])
