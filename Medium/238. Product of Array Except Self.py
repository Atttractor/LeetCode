"""
Medium

Given an integer array nums and an integer k, return the k most frequent elements.
You may return the answer in any order.

Runtime: 84.69% 230ms
Memory: 46.44% 23.6MB
"""
from collections import Counter
from typing import List


class Solution:
    @staticmethod
    def productExceptSelf(nums: List[int]) -> List[int]:
        n = len(nums)
        zero_count = nums.count(0)
        miltiplication = 1
        for num in nums:
            if num != 0:
                miltiplication *= num

        if zero_count >= 2:
            return [0] * n
        elif zero_count == 1:
            mas = [0] * n
            mas[nums.index(0)] = miltiplication
            return mas
        else:
            return [miltiplication // num for num in nums]


if __name__ == '__main__':
    Solution.productExceptSelf([1, 2, 3, 4])
