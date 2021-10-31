from queue import Queue


class Stack:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()
        self.current_size = 0

    def push(self, val):
        self.current_size += 1
        self.q2.put(val)

        # Put all value in the q1 from q2
        while (not self.q1.empty()):
            self.q2.put(self.q1.queue[0])
            self.q1.get()

        # Swap the q1 and q2
        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        self.current_size -= 1
        return self.q1.get()

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
