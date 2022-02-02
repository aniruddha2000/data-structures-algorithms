class Solution:
    def maximumTime(self, time: str) -> str:
        result = list(time)
        for i, n in enumerate(time):
            if n != "?" or n == ":":
                continue
            if i == 0:
                result[i] = "2" if result[1] in "?0123" else "1"
            if i == 1:
                result[i] = "3" if result[0] == "2" else "9"
            if i == 3:
                result[i] = "5"
            if i == 4:
                result[i] = "9"
        return "".join(result)


obj = Solution()
print(obj.maximumTime("2?:?0"))
print(obj.maximumTime("0?:3?"))
print(obj.maximumTime("1?:22"))
