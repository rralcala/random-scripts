from queue import Queue
import threading
import time

q = Queue()


class Worker(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        while(True):
            print(q.get())
            q.task_done()


if __name__ == '__main__':
    for w in range(10):
        t = Worker()
        t.daemon = True
        t.start()

    for i in range(1000):
        q.put(i)

    time.sleep(10)
    for i in range(1000, 2000):
        q.put(i)
    q.join()
