"""
Easy
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all
the original letters exactly once.

Runtime: % ms
Memory: % MB
"""
from typing import List


class Solution:
    @staticmethod
    def isAnagram(s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        d1, d2 = {}, {}
        for i in range(len(s)):
            d1[s[i]] = 1 if s[i] not in d1 else d1[s[i]] + 1
            d2[t[i]] = 1 if t[i] not in d2 else d2[t[i]] + 1

        return d1 == d2


if __name__ == '__main__':
    print(Solution.isAnagram('anagrfam', 'nagaram'))
