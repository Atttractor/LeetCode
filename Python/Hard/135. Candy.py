"""
Hard
There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:
* Each child must have at least one candy.
* Children with a higher rating get more candies than their neighbors.

Return the minimum number of candies you need to have to distribute the candies to the children.

Runtime: 29.81% 60ms
Memory: 50.33% 16.5MB
"""
from typing import List


class Solution:
    # Я пытался, но не смог, а какой-то чел решил это за два условия. ТИЛЬТ ЖОСКИЙ
    # Я потратил на это 4 часа своей жизни
    @staticmethod
    def candy(ratings: List[int]) -> int:
        candies = [1 for _ in range(len(ratings))]

        if len(ratings) == 0:
            return 0

        if len(ratings) == 1:
            return 1

        if ratings[1] < ratings[0]:
            candies[0] = 2

        i = 1
        while i < len(ratings):
            if i == len(ratings) - 1:
                if ratings[i - 1] < ratings[i]:
                    candies[i] = candies[i - 1] + 1
            else:
                if ratings[i - 1] == ratings[i] == ratings[i + 1]:
                    candies[i] = 1
                elif ratings[i - 1] == ratings[i] < ratings[i + 1]:
                    candies[i] = candies[i - 1]
                elif ratings[i - 1] == ratings[i] > ratings[i + 1]:
                    if candies[i] == candies[i + 1]:
                        candies[i] = candies[i + 1] + 1
                elif ratings[i - 1] < ratings[i] == ratings[i + 1]:
                    candies[i] = candies[i - 1] + 1
                elif ratings[i - 1] < ratings[i] < ratings[i + 1]:
                    candies[i] = candies[i - 1] + 1
                elif ratings[i - 1] < ratings[i] > ratings[i + 1]:
                    candies[i] = max(candies[i - 1], candies[i + 1]) + 1
                elif ratings[i - 1] > ratings[i] == ratings[i + 1]:
                    candies[i] = candies[i - 1] - 1
                elif ratings[i - 1] > ratings[i] < ratings[i + 1]:
                    candies[i] = min(candies[i - 1], candies[i + 1]) - 1
                    if candies[i] < 1:
                        candies[i] = 1
                elif ratings[i - 1] > ratings[i] > ratings[i + 1]:
                    if candies[i - 1] - candies[i] == candies[i + 1]:
                        k = i
                        while ratings[k - 1] > ratings[k]:
                            candies[k - 1] += 1
                            k -= 1
                        candies[i] += 1
                    else:
                        candies[i] = candies[i - 1] - 1
            i += 1

        for i in range(1, len(ratings) - 1):
            if ratings[i - 1] > ratings[i] > ratings[i + 1]:
                candies[i] = candies[i + 1] + 1

        print(f'candies - {candies}')

        return sum(candies)

    @staticmethod
    def hz(ratings: List[int]) -> int:
        n = len(ratings)
        give = [1] * n

        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                give[i] = give[i - 1] + 1

        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1] and give[i] <= give[i + 1]:
                give[i] = give[i + 1] + 1

        return sum(give)

if __name__ == '__main__':
    # Solution.candy([1, 3, 2, 2, 1])  # [1, 2, 1, 2, 1]
    # Solution.candy([1, 0, 2])  # [2, 1, 2]
    # Solution.candy([1, 2, 2])  # [1, 2, 1]
    # Solution.candy([1, 2, 3, 3, 3, 2, 1])  # [1, 2, 3, 1, 3, 2, 1]
    # Solution.candy([29, 51, 87, 87, 72, 12])  # [1, 2, 3, 3, 2, 1]
    # Solution.candy([1, 6, 10, 8, 7, 3, 2])  # [1, 2, 5, 4, 3, 2, 1]
    # Solution.candy([1, 2, 3, 5, 4, 3, 2, 1])  # []
    Solution.hz([58, 21, 72, 77, 48, 9, 38, 71, 68, 77, 82, 47, 25, 94, 89, 54, 26, 54, 54, 99, 64, 71, 76, 63,
                    81, 82, 60, 64, 29, 51, 87, 87, 72, 12, 16, 20, 21, 54, 43, 41, 83, 77, 41, 61, 72, 82, 15, 50,
                    36, 69, 49, 53, 92, 77, 16, 73, 12, 28, 37, 41, 79, 25, 80, 3, 37, 48, 23, 10, 55, 19, 51, 38,
                    96, 92, 99, 68, 75, 14, 18, 63, 35, 19, 68, 28, 49, 36, 53, 61, 64, 91, 2, 43, 68, 34, 46, 57,
                    82, 22, 67, 89])
    # АААААААААААА СЛОЖНА БЛЯ
