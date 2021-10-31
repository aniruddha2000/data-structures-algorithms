from queue import Queue


class Stack:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()
        self.current_size = 0

    def push(self, val):
        self.q1.put(val)
        self.current_size += 1

    def pop(self):
        if self.q1.empty():
            return "Underflow!"
        while (self.q1.qsize() != 1):
            self.q2.put(self.q1.get())
        self.q1.get()
        self.current_size -= 1

        self.q1, self.q2 = self.q2, self.q1

    def display(self):
        print()
        if self.q1.empty():
            print("Queue is empty!")
        for i in self.q1.queue:
            print(i, end="=>")


if __name__ == "__main__":
    s = Stack()
    s.display()
    s.push(7)
    s.push(8)
    s.push(9)
    s.display()
    s.pop()
    s.display()
