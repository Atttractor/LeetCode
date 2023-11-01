"""
Easy

Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two
different nodes in the tree.

Runtime: % ms
Memory: % MB
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        pass  # Ты не решил


if __name__ == '__main__':
    Solution.getMinimumDifference([4, 1, -1, 2, -1, 2, 3], 2)
