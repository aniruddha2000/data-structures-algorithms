from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:

        water = 0
        start = 0
        end = len(height) - 1

        while start < end:
            water = max(water, min(height[start], height[end]) * (end - start))
            if height[end] > height[start]:
                start += 1
            else:
                end -= 1
        return water


obj = Solution()
print(obj.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(obj.maxArea([1, 1]))
print(obj.maxArea([1, 2, 1]))
print(obj.maxArea([2, 3, 4, 5, 18, 17, 6]))
