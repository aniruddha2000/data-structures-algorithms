from string import ascii_lowercase


class Solution:
    def minTimeToType(self, word: str) -> int:
        pointer = "a"
        type = 0
        movePointer = 0
        for char in word:
            if pointer == char:
                type += 1
            else:
                diff = abs(ascii_lowercase.index(pointer) - ascii_lowercase.index(char))
                movePointer += min(diff, (26 - diff))
                type += 1
                pointer = char
        return type + movePointer


obj = Solution()
print(obj.minTimeToType("abc"))
print(obj.minTimeToType("bza"))
print(obj.minTimeToType("zjpc"))
