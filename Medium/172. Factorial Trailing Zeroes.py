"""
Medium
Given an integer n, return the number of trailing zeroes in n!.

Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.

Runtime: 42.23% 53ms
Memory: 19.42% 16.4MB
"""
import math


class Solution:
    @staticmethod
    def trailingZeroes(n: int) -> int:
        res = 0
        while n > 0:
            n = n // 5
            res += n
        print(res)


if __name__ == '__main__':
    Solution.trailingZeroes(7)

