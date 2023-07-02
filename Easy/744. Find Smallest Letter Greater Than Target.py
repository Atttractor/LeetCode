"""
Easy
You are given an array of characters letters that is sorted in non-decreasing order, and a character target. There are
at least two different characters in letters.

Return the smallest character in letters that is lexicographically greater than target. If such a character does not
exist, return the first character in letters.

Runtime: 32.2% 139ms
Memory: 21.82% 16.8MB
"""
from typing import List


class Solution:
    @staticmethod
    def nextGreatestLetter(letters: List[str], target: str) -> str:
        if target < letters[0] or target >= letters[-1]:
            return letters[0]

        left_cursor = 0
        right_cursor = len(letters) - 1

        while left_cursor + 1 < right_cursor:
            mid = left_cursor + (right_cursor - left_cursor) // 2
            if letters[mid] > target:
                right_cursor = mid
            else:
                left_cursor = mid

        return letters[right_cursor]


if __name__ == '__main__':
    Solution.nextGreatestLetter(["c", "f", "j"], 'j')  # c
