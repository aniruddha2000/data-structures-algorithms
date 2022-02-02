from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        right = 0
        last = len(nums) - 1
        for i in range(len(nums)):
            if i > right:
                return False
            if i + nums[i] > right:
                right = nums[i] + i
            if right >= last:
                return True


obj = Solution()
print(obj.canJump([2, 3, 1, 1, 4]))
print(obj.canJump([3, 2, 1, 0, 4]))
