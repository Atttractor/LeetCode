"""
Medium
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
(you may want to display this pattern in a fixed font for better legibility)
"""


class Solution:
    @staticmethod
    def convert(s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        result = ''
        for i in range(numRows):
            if i == 0 or i == numRows - 1:
                result += s[i::2 * (numRows - 1)]
            else:
                if numRows % 2 == 1 and numRows + 1 / 2 == i:
                    result += s[i::numRows - 1]
                else:
                    # It's buf1 and buf2 is very bad idea, but I have not figured out how to do it otherwise
                    buf1 = s[i::2 * (numRows - 1)]
                    buf2 = s[(2 * (numRows - 1)) - i::2 * (numRows - 1)]
                    # Это пиздец, чево я тут наделал
                    result += ''.join([buf1[i] + buf2[i]
                                       for i in range(len(buf2) if len(buf1) > len(buf2) else len(buf1))])
                    if len(buf1) > len(buf2):
                        result += buf1[-1]
                    elif len(buf2) > len(buf1):
                        result += buf2[-1]
        return result

    @staticmethod
    def get_zig_zag_mas(n: str):
        mas = [[0 for _ in range(30)] for _ in range(n)]
        k = 1
        p = n - 2
        for i in range(30):
            if i % (n - 1) == 0:
                for j in range(n):
                    mas[j][i] = k
                    k += 1
                    p = n - 2
            else:
                mas[p][i] = k
                p -= 1
                k += 1

        for i in mas:
            print(i)


if __name__ == '__main__':
    Solution.get_zig_zag_mas(5)
    Solution.convert('ABCDEF', 5)
