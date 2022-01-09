from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g = sorted(g)
        s = sorted(s)
        numberOfChildren = len(g)
        numberOfCookies = len(s)
        cookie = 0
        ans = 0
        i = 0
        while i < numberOfChildren and cookie < numberOfCookies:
            if s[cookie] >= g[i]:
                i += 1
                ans += 1
            cookie += 1
        return ans


obj = Solution()
print(obj.findContentChildren([1, 2, 3], [1, 1]))
print(obj.findContentChildren([1, 2], [1, 2, 3]))
