from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        minOp = 0
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                continue
            diff = nums[i - 1] - nums[i]
            nums[i] += diff + 1
            minOp += diff + 1
        return minOp


obj = Solution()
print(obj.minOperations([1, 1, 1]))
print(obj.minOperations([1, 5, 2, 4, 1]))
print(obj.minOperations([8]))
