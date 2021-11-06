class OptimalMergePAttern:
    def __init__(self, items: list) -> None:
        self.items = items
        self.totalMergeValue = 0

    def solve(self) -> int:
        while len(self.items) > 2:
            self.items.sort()
            firstElement = self.items.pop(0)
            secondElement = self.items.pop(0)
            sumOfFirstAndSecond = firstElement + secondElement
            self.totalMergeValue += sumOfFirstAndSecond
            self.items.append(sumOfFirstAndSecond)
        remainElemnt1 = self.items.pop()
        remainElemnt2 = self.items.pop()
        self.totalMergeValue += remainElemnt1 + remainElemnt2
        return self.totalMergeValue


testCase1 = [10, 20, 30]
instance1 = OptimalMergePAttern(testCase1)
print(instance1.solve())

testCase2 = [6, 5, 2, 3]
instance2 = OptimalMergePAttern(testCase2)
print(instance2.solve())

testCase3 = [20, 30, 10, 5, 30]
instance3 = OptimalMergePAttern(testCase3)
print(instance3.solve())
