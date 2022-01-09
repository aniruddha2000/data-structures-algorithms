from typing import List


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums = sorted(nums)
        n = len(nums)
        for i in range(1, len(nums) - 1):
            if nums[n - i - 2] + nums[n - i - 1] > nums[n - i]:
                return nums[n - i - 2] + nums[n - i - 1] + nums[n - i]
        return 0


obj = Solution()
# print(obj.largestPerimeter([2, 1, 2]))
# print(obj.largestPerimeter([1, 2, 1]))
print(obj.largestPerimeter([1, 1, 5, 2, 3]))
