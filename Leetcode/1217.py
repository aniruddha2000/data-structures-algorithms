from typing import List


class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        even = 0
        odd = 0
        for coin in position:
            if coin % 2 == 0:
                even += 1
            else:
                odd += 1
        return min(odd, even)
