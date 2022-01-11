from typing import List


class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        sum = 0
        for i in range(len(nums)):
            if nums[i] < 0 and k > 0:
                nums[i] = -1 * nums[i]
                k -= 1
        for num in nums:
            sum += num

        _min = min(nums)
        if k % 2 != 0:
            sum -= 2 * _min

        return sum


obj = Solution()
print(obj.largestSumAfterKNegations([4, 2, 3], 1))
print(obj.largestSumAfterKNegations([3, -1, 0, 2], 3))
print(obj.largestSumAfterKNegations([2, -3, -1, 5, -4], 2))
