from typing import List


class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums = sorted(nums, reverse=True)
        res = []
        _sum = 0
        for num in nums:
            _sum += num
            res.append(num)
            if _sum > sum(nums) - _sum:
                break
        return res


obj = Solution()
print(obj.minSubsequence([4, 3, 10, 9, 8]))
print(obj.minSubsequence([4, 4, 7, 6, 7]))
