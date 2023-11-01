# Ответом тут является последовательность Фибоначи

class Solution:
    @staticmethod
    def climbStairs(n: int) -> int:
        if n <= 0:
            return 0
        result = 1
        prev = 1
        for i in range(n - 1):
            buf = result
            result += prev
            prev = buf
        return result

    @staticmethod
    def recursion(n: int) -> int:
        def fib(num: int) -> int:
            if num == 2:
                return 2
            if num == 1:
                return 1
            return fib(num - 2) + fib(num - 1)
        return fib(n)


if __name__ == '__main__':
    print(Solution.climbStairs(0))
