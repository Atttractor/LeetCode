"""
Easy
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Runtime: % ms
Memory: % MB
"""
from typing import List


class Solution:
    @staticmethod
    def twoSum(nums: List[int], target: int) -> List[int]:
        d = {i: target - nums[i] for i in range(len(nums))}
        print(d)
        for i in range(len(nums)):
            if d[i] in nums and i != nums.index(d[i]):
                return [i, nums.index(d[i])]


if __name__ == '__main__':
    print(Solution.twoSum([3, 2, 4], 6))
