"""
Medium

Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are
equal.

A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).

Runtime: 19.92% 732ms
Memory: 82.96% 21.2MB
"""
from typing import List


class Solution:
    @staticmethod
    def equalPairs(grid: List[List[int]]) -> int:
        n = len(grid)
        rows = {i: grid[i] for i in range(n)}
        columns = list(zip(*grid))
        result = 0

        for i in range(n):
            result += list(rows.values()).count(list(columns[i]))

        return result


if __name__ == '__main__':
    Solution.equalPairs([[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]])
