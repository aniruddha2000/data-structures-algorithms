class Solution:
    def largestOddNumber(self, num: str) -> str:
        odd = ["1", "3", "5", "7", "9"]
        for i, n in reversed(list(enumerate(num))):
            if n in odd:
                return num[0 : i + 1]
        return ""


obj = Solution()
print(obj.largestOddNumber("52"))
print(obj.largestOddNumber("4260"))
print(obj.largestOddNumber("35427"))
