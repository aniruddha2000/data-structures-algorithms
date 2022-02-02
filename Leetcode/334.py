from sys import maxsize
from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = maxsize
        second = maxsize
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        return False


obj = Solution()
print(obj.increasingTriplet([1, 2, 3, 4, 5]))
print(obj.increasingTriplet([5, 4, 3, 2, 1]))
print(obj.increasingTriplet([2, 1, 5, 0, 4, 6]))
