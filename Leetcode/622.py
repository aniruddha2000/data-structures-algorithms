class MyCircularQueue:
    def __init__(self, k: int):
        self.k = [-1 for i in range(k)]
        self.front, self.rear = -1, -1
        self.size = k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.isEmpty():
            self.front = 0
        self.rear = (self.rear + 1) % self.size
        self.k[self.rear] = value
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        if self.front == self.rear:
            self.front, self.rear = -1, -1
            return True
        else:
            self.front = (self.front + 1) % self.size
            return True

    def Front(self) -> int:
        return self.k[self.front]

    def Rear(self) -> int:
        return self.k[self.rear]

    def isEmpty(self) -> bool:
        if self.front == -1 and self.rear == -1:
            return True
        return False

    def isFull(self) -> bool:
        if (self.rear + 1) % self.size == self.front:
            return True
        return False


m = MyCircularQueue(3)
print(m.enQueue(1))
print(m.enQueue(2))
print(m.enQueue(3))
print(m.enQueue(4))
# print(m.Rear())
# print(m.isFull())
print(m.deQueue())
print(m.deQueue())
print(m.enQueue(3))
print(m.enQueue(5))
print(m.deQueue())
print(m.deQueue())
print(m.deQueue())
print(m.deQueue())
# print(m.Rear())
