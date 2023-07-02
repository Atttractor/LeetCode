# Ответом тут является последовательность Фибоначи
from typing import List, Tuple


class Solution:
    @staticmethod
    def checkStraightLine(coordinates: List[List[int]]) -> bool:
        def get_params_of_line(cord1: List[int], cord2: List[int]) -> List[float]: #
            if cord1[0] == cord2[0]:
                return 'vert', 'ical'
            elif (cord2[0] - cord1[0]) == 0:
                a = 0
            else:
                a = (cord2[1] - cord1[1]) / (cord2[0] - cord1[0])
            return a, cord1[1] - cord1[0] * a

        k, b = get_params_of_line(coordinates[0], coordinates[1])

        for i in range(1, len(coordinates) - 1):
            buf_k, buf_b = get_params_of_line(coordinates[i], coordinates[i + 1])
            if buf_k != k or buf_b != b:
                return False
        return True


if __name__ == '__main__':
    mas = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [1, 2], [1, 1]]
    mas1 = [[0, 0], [0, 1], [0, -1]]
    mas2 = [[2, 1], [4, 2], [6, 3]]
    print(Solution.checkStraightLine(mas1))
