from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        l = 0
        r = 0

        while r < len(nums) - 1:
            furthest = 0

            for i in range(l, r + 1):
                furthest = max(furthest, i + nums[i])
            l = r + 1
            r = furthest
            res += 1
        return res


obj = Solution()
print(obj.jump([2, 3, 1, 1, 4]))
print(obj.jump([2, 3, 0, 1, 4]))
