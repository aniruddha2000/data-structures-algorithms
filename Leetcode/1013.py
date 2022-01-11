from typing import List


class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        sum = 0
        for ar in arr:
            sum += ar

        if sum % 3 != 0:
            return False
        else:
            i = 0
            noOfPart = 0
            for _ in range(3):
                continuousSum = 0
                while i != len(arr):
                    continuousSum += arr[i]
                    if continuousSum == sum / 3:
                        noOfPart += 1
                        i += 1
                        break
                    i += 1
        if noOfPart < 3:
            return False
        else:
            return True


obj = Solution()
print(obj.canThreePartsEqualSum([0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1]))
print(obj.canThreePartsEqualSum([0, 2, 1, -6, 6, 7, 9, -1, 2, 0, 1]))
print(obj.canThreePartsEqualSum([3, 3, 6, 5, -2, 2, 5, 1, -9, 4]))
