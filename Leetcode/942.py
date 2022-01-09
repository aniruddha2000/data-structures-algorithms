from typing import List


class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        size = len(s)
        low = 0
        high = size

        res = [-1] * (size + 1)
        for i, c in enumerate(s):
            if c == "I":
                res[i] = low
                low += 1
            else:
                res[i] = high
                high -= 1
        res[size] = low
        return res


obj = Solution()
print(obj.diStringMatch("IDID"))
print(obj.diStringMatch("III"))
print(obj.diStringMatch("DDI"))
