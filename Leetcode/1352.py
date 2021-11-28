class ProductOfNumbers:
    def __init__(self):
        self.list = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.list = [1]
            return
        self.list.append(self.list[-1] * num)

    def getProduct(self, k: int) -> int:
        if len(self.list) <= k:
            return 0
        return self.list[-1] // self.list[-1 - k]


obj = ProductOfNumbers()
obj.add(3)
obj.add(0)
obj.add(2)
obj.add(5)
obj.add(4)
print(obj.getProduct(2))
print(obj.getProduct(3))
print(obj.getProduct(4))
obj.add(8)
print(obj.getProduct(2))
