class FrontMiddleBackQueue:
    def __init__(self):
        self.q = []

    def pushFront(self, val: int) -> None:
        self.q.insert(0, val)

    def pushMiddle(self, val: int) -> None:
        if len(self.q) % 2 == 1:
            self.q.insert(int(len(self.q) / 2), val)
        else:
            self.q.insert((int(len(self.q) / 2)), val)

    def pushBack(self, val: int) -> None:
        self.q.append(val)

    def popFront(self) -> int:
        if len(self.q) == 0:
            return -1
        res = self.q[0]
        self.q = self.q[1:]
        return res

    def popMiddle(self) -> int:
        if len(self.q) == 0:
            return -1
        middle = int(len(self.q) / 2)
        if len(self.q) % 2 == 1:
            res = self.q[middle]
            self.q = self.q[0:middle] + self.q[middle + 1 :]
            return res
        else:
            middle -= 1
            res = self.q[middle]
            self.q = self.q[0:middle] + self.q[middle + 1 :]
            return res

    def popBack(self) -> int:
        if len(self.q) == 0:
            return -1
        return self.q.pop()


obj = FrontMiddleBackQueue()
obj.pushFront(1)
obj.pushBack(2)
obj.pushMiddle(3)
obj.pushMiddle(4)
obj.popFront()
obj.popMiddle()
obj.popMiddle()
obj.popBack()
obj.popFront()
