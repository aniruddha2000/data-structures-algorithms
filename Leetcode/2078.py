from typing import List


class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        lastHouse = colors[-1]
        houseOne = len(colors) - 1
        houseTwo = 0
        for i, color in enumerate(colors):
            if color != lastHouse:
                houseTwo = i
                break
        rightToLeft = abs(houseOne - houseTwo)

        firstHouse = colors[0]
        houseOne = 0
        houseTwo = 0
        i = len(colors) - 1
        while i != 0:
            if colors[i] != firstHouse:
                houseTwo = i
                break
            i -= 1
        leftToRight = abs(houseOne - houseTwo)

        return max(leftToRight, rightToLeft)


obj = Solution()
print(obj.maxDistance([1, 1, 1, 6, 1, 1, 1]))
print(obj.maxDistance([1, 8, 3, 8, 3]))
print(obj.maxDistance([0, 1]))
print(obj.maxDistance([6, 6, 6, 6, 6, 6, 6, 6, 6, 19, 19, 6, 6]))
