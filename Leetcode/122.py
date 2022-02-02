from turtle import pen
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 1
        profit = 0
        while i < len(prices):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
            i += 1

        return profit


obj = Solution()
print(obj.maxProfit([7, 1, 5, 3, 6, 4]))
print(obj.maxProfit([1, 2, 3, 4, 5]))
