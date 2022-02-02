from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        numstr = sorted([str(num) for num in nums])
        curr = [numstr[0]]
        for i in range(1, len(nums)):
            if curr[-1] + numstr[i] > numstr[i] + curr[-1]:
                numstr[i - len(curr)] = numstr[i]
                numstr[i] = curr[-1]
            elif curr[-1] + numstr[i] == numstr[i] + curr[-1]:
                curr.append(numstr[i])
            else:
                curr = [numstr[i]]

        result = "".join(reversed(numstr))
        if int(result) > 0:
            return result
        else:
            return "0"


obj = Solution()
print(obj.largestNumber([10, 2]))
print(obj.largestNumber([3, 30, 34, 5, 9]))
