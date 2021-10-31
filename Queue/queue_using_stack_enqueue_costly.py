class Queue:
    def __init__(self) -> None:
        self.s1 = []
        self.s2 = []

    def enQueue(self, val):
        self.s2.append(val)

        # Transfer all value from s1 to s2
        while (len(self.s1) != 0):
            self.s2.append(self.s1.pop(0))

        # Swap s1 with s2
        self.s1, self.s2 = self.s2, self.s1

    def deQueue(self):
        if (len(self.s1) == 0):
            print("Queue empty")
        self.s1.pop()

    def display(self):
        if (len(self.s1) == 0):
            print("Queue empty")
        else:
            for i in self.s1:
                print(i, end="=>")
            print("NULL")


if __name__ == "__main__":
    q1 = Queue()
    q1.display()
    q1.enQueue(10)
    q1.enQueue(15)
    q1.enQueue(20)
    q1.display()
    q1.deQueue()
    q1.deQueue()
    q1.display()
    q1.enQueue(25)
    q1.display()
