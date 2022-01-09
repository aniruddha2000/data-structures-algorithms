from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        _dict = {5: 0, 10: 0, 20: 0}
        for i in bills:
            if i == 5:
                _dict[5] += 1
            elif i == 10:
                if _dict[5] == 0:
                    return False
                _dict[5] -= 1
                _dict[10] += 1
            else:
                if _dict[10] > 0 and _dict[5] > 0:
                    _dict[5] -= 1
                    _dict[10] -= 1
                elif _dict[5] >= 3:
                    _dict[5] -= 3
                else:
                    return False
        return True
