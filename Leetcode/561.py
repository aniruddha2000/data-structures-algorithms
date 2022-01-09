from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums)
        i = 0
        ans = 0
        while i < len(nums):
            ans += min(nums[i], nums[i + 1])
            i += 2
        print(ans)


obj = Solution()
obj.arrayPairSum([1, 4, 3, 2])
obj.arrayPairSum([6, 2, 6, 5, 1, 2])
