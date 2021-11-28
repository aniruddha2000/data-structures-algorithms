from collections import deque
from typing import List


class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        d = deque()
        deck.sort(reverse=True)
        for i in deck:
            if d:
                d.appendleft(d.pop())
            d.appendleft(i)
        return list(d)


obj = Solution()
print(obj.deckRevealedIncreasing([17, 13, 11, 2, 3, 5, 7]))
