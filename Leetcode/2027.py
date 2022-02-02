class Solution:
    def minimumMoves(self, s: str) -> int:
        if "X" not in s:
            return 0

        totalMove = 0
        i = 0
        while i < len(s):
            if s[i] == "X":
                totalMove += 1
                i += 3
                continue
            i += 1

        return totalMove


obj = Solution()
print(obj.minimumMoves("XXX"))
print(obj.minimumMoves("XXOX"))
print(obj.minimumMoves("OOOO"))
