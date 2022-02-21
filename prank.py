from threading import Thread


class MyThread(Thread):
    def __init__(self, name) -> None:
        Thread.__init__(self)
        self.name = name

    def run(self):
        for i in range(10000000000000):
            msg = "%s thread is running" % self.name
            print(msg)


def create_thread():
    for i in range(1000000):
        name = "Thread #%s" % (i + 1)
        my_thread = MyThread(name)
        my_thread.start()


if __name__ == "__main__":
    create_thread()
