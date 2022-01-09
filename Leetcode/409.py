class Solution:
    def longestPalindrome(self, s: str) -> int:
        res = 0
        findOdd = False
        counter = {}
        for c in s:
            counter[c] = counter.get(c, 0) + 1

        values = sorted(counter.values(), reverse=True)
        # print(values)
        for value in values:
            if value % 2 == 0:
                res += value
            else:
                res += value - 1
                findOdd = True
        if findOdd:
            return res + 1
        return res


obj = Solution()
# print(obj.longestPalindrome("abccccdd"))
print(obj.longestPalindrome("aaaabbbbbbcccdfffffff"))
