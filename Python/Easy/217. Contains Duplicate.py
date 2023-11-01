"""
Easy
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every
element is distinct.

Runtime: 40.78% 559ms
Memory: 20.13% 31.9MB
"""
from typing import List


class Solution:
    @staticmethod
    def containsDuplicate(nums: List[int]) -> bool:
        if len(set(nums)) < len(nums):
            return True
        else:
            return False


if __name__ == '__main__':
    Solution.containsDuplicate([1, 2, 3, 4, 1])
