"""
Easy

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all
the original letters exactly once.

Runtime: 86.23% 105ms
Memory: 88.41% 19.4MB
"""
from typing import List


class Solution:
    @staticmethod
    def groupAnagrams(strs: List[str]) -> List[List[str]]:
        d = {}
        for string in strs:
            s = ''.join(sorted(string))
            if s not in d:
                d[s] = [string]
            else:
                d[s].append(string)

        return list(d.values())


if __name__ == '__main__':
    Solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
