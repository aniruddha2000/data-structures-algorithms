class Queue:
    def __init__(self) -> None:
        self.s1 = []
        self.s2 = []

    def enQueue(self, val):
        self.s1.append(val)

    def deQueue(self):
        if (len(self.s1) == 0):
            print("Queue empty")

        # Transfer all value from s1 to s2
        while (len(self.s1) != 0):
            self.s2.append(self.s1.pop())

        # Pop out the first element added
        self.s2.pop()

        # Get all element back to s1 in correct order
        while (len(self.s2) != 0):
            self.s1.append(self.s2.pop())

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
