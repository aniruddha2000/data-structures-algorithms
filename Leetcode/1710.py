from typing import List


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        totalUnit = 0
        remainingSize = truckSize
        for box, unit in boxTypes:
            if remainingSize == 0:
                break
            else:
                if box < remainingSize or box == remainingSize:
                    remainingSize -= box
                    totalUnit += box * unit
                else:
                    totalUnit += remainingSize * unit
                    remainingSize = 0
        return totalUnit


obj = Solution()
print(obj.maximumUnits([[1, 3], [2, 2], [3, 1]], 4))
print(obj.maximumUnits([[5, 10], [2, 5], [4, 7], [3, 9]], 10))
