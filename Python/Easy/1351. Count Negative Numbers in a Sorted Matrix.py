"""
Easy
Task: Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise,
return the number of negative numbers in grid.
Follow up: Could you find an O(n + m) solution?
Runtime: 32.21% 136ms
Memory: 14.16% 17.6MB
"""
from typing import List


class Solution:
    @staticmethod
    def countNegatives(grid: List[List[int]]) -> int:
        result = 0
        i = len(grid) - 1
        j = 0

        while i >= 0 and j < len(grid[0]):
            if grid[i][j] < 0:
                result += len(grid[0]) - j
                i -= 1
            else:
                j += 1

        return result


if __name__ == '__main__':
    Solution.countNegatives([[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]])
