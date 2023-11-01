import re


class Solution:
    @staticmethod
    def isValid(s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        stack = []
        d = {')': '(', ']': '[', '}': '{'}
        for i in s:
            if i == '(' or i == '[' or i == '{':
                stack.append(i)
            elif i == ')' or i == ']' or i == '}':
                if stack:
                    if stack[-1] == d[i]:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        if stack:
            return False
        else:
            return True


if __name__ == '__main__':
    print(Solution.isValid('([}}])'))
