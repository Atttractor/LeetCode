"""
Easy
You are given an array of characters letters that is sorted in non-decreasing order, and a character target. There are
at least two different characters in letters.

Return the smallest character in letters that is lexicographically greater than target. If such a character does not
exist, return the first character in letters.

Runtime: 61.2% 142ms
Memory: 50.46% 19MB
"""
from typing import List
from collections import Counter


class Solution:
    # А я и не знал что так можно делать
    @staticmethod
    def singleNumber(nums: List[int]) -> int:
        n = 0
        for num in nums:
            n ^= num
        return n


if __name__ == '__main__':
    Solution.singleNumber([5])
