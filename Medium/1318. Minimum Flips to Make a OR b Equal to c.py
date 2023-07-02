"""
Medium
Given 3 positives numbers a, b and c. Return the minimum flips required in some bits of a and b to make ( a
OR b == c ). (bitwise OR operation). Flip operation consists of change any single bit 1 to 0 or change the bit 0 to 1
in their binary representation.
"""


class Solution:
    @staticmethod
    def minFlips(a: int, b: int, c: int) -> int:
        sum_of_a_and_b = a | b
        diff_of_c_and_sum = c ^ sum_of_a_and_b

        bin_of_sum = list(bin(sum_of_a_and_b)[:1:-1])
        bin_of_diff = list(bin(diff_of_c_and_sum)[:1:-1])
        bin_a = list(bin(a)[:1:-1])
        bin_b = list(bin(b)[:1:-1])
        bin_c = list(bin(c)[:1:-1])
        bin_a.extend(['0' for _ in range(len(bin_of_diff) - len(bin_a))])
        bin_b.extend(['0' for _ in range(len(bin_of_diff) - len(bin_b))])
        bin_c.extend(['0' for _ in range(len(bin_of_diff) - len(bin_c))])

        print(f'Всё перевёрнуто\n'
              f'a - \t\t{bin_a}\n'
              f'b - \t\t{bin_b}\n'
              f'c - \t\t{bin_c}\n'
              f'сумма a и b - {bin_of_sum}\n'
              f'разность c и суммы - {bin_of_diff}\n')

        k = 0
        for index, num in enumerate(bin_of_diff):
            if num == '1':
                if bin_c[index] == '0':
                    if bin_a[index] == '1' and bin_b[index] == '1':
                        k += 2
                    elif bin_a[index] == '1' or bin_b[index] == '1':
                        k += 1
                elif bin_c[index] == '1':
                    k += 1
        print(k)
        return k

    @staticmethod
    def ne_moyo(a: int, b: int, c: int) -> int:
        # Гениально ЛОЛ
        count = lambda x: bin(x).count('1')
        return count((a | b) ^ c) + count(a & b & ~c)


if __name__ == '__main__':
    Solution.minFlips(8, 3, 5)
