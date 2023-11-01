"""
Easy
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters.
No two characters may map to the same character, but a character may map to itself.

Runtime: 55.32% 53ms
Memory: 52.64% 16.6MB
"""


class Solution:
    @staticmethod
    def isIsomorphic(s: str, t: str) -> bool:
        if len(s) != len(t) or len(set(s)) != len(set(t)):
            return False

        d = {s[i]: t[i] for i in range(len(s))}

        for index, alpha in enumerate(s):
            if d[alpha] != t[index]:
                return False

        return True

    @staticmethod
    def isIsomorphic_two(s: str, t: str) -> bool:
        # Это решение проиграло и по памяти и по времени, но по идее тут я использую for 1 раз, а не два
        if len(s) != len(t) or len(set(s)) != len(set(t)):
            return False

        d = {}

        for i in range(len(s)):
            if s[i] not in d.keys():
                d[s[i]] = t[i]
            else:
                if d[s[i]] != t[i]:
                    return False

        return True


if __name__ == '__main__':
    print(Solution.isIsomorphic('egg', 'add'))
