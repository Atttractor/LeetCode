"""
Easy
Given a pattern and a string s, find if s follows the same pattern.
Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

Runtime: 45.17% 46ms
Memory: 23.43% 16.4MB
"""


class Solution:
    @staticmethod
    def wordPattern(pattern: str, s: str) -> bool:
        list_patter = list(pattern)
        list_string = s.split(' ')

        d = {}
        for i in range(len(list_patter)):
            if list_string[i] not in d.values():
                d[list_patter[i]] = list_string[i]

        try:
            if ' '.join([d[i] for i in list_patter]) != s:
                return False
            else:
                return True
        except KeyError:
            return False


if __name__ == '__main__':
    print(Solution.wordPattern('abba', 'dog dog dog dog'))
