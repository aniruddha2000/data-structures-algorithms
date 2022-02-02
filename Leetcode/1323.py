class Solution:
    def maximum69Number(self, num: int) -> int:
        num = [int(x) for x in str(num)]
        for i, n in enumerate(num):
            if n == 6:
                num[i] = 9
                break
        s = [str(x) for x in num]
        return int("".join(s))


obj = Solution()
print(obj.maximum69Number(9669))
print(obj.maximum69Number(9996))
print(obj.maximum69Number(9999))
