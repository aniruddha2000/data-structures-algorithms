class Solution:
    def balancedStringSplit(self, s: str) -> int:
        ans = 0
        balance = 0
        for c in s:
            if balance == 0:
                ans += 1
            if c == "L":
                balance += 1
            else:
                balance -= 1
        return ans


obj = Solution()
print(obj.balancedStringSplit("RLRRLLRLRL"))
print(obj.balancedStringSplit("RLLLLRRRLR"))
print(obj.balancedStringSplit("LLLLRRRR"))
