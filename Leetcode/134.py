from cmath import tan
from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start = 0
        gr = 0
        shortage = 0
        tank = 0
        for i in range(len(gas)):
            gr = gas[i] - cost[i]
            tank += gr
            if tank < 0:
                start += i
                tank = 0
            shortage += gr
        if shortage >= 0:
            return start
        return -1


obj = Solution()
print(obj.canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))
# print(obj.canCompleteCircuit([2, 3, 4], [3, 4, 3]))
