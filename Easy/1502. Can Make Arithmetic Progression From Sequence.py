"""
Easy
A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the
same. Given an array of numbers arr, return true if the array can be rearranged to form an arithmetic progression.
Otherwise, return false

Runtime: 29.81% 60ms
Memory: 50.33% 16.5MB
"""


class Solution:
    @staticmethod
    def canMakeArithmeticProgression(arr: List[int]) -> bool:
        arr.sort()
        diff = arr[1] - arr[0]
        for i in range(1, len(arr) - 1):
            if arr[i + 1] - arr[i] != diff:
                return False
        return True


if __name__ == '__main__':
    Solution.canMakeArithmeticProgression([5, 3, 1, 0])
