"""
Medium

Given an integer array nums and an integer k, return the k most frequent elements.
You may return the answer in any order.

Runtime: 87.69% 107ms
Memory: 52.18% 21.2MB
"""
from collections import Counter
from typing import List


class Solution:
    @staticmethod
    def topKFrequent(nums: List[int], k: int) -> List[int]:
        return [i[0] for i in Counter(nums).most_common(k)]


if __name__ == '__main__':
    Solution.topKFrequent([4, 1, -1, 2, -1, 2, 3], 2)
