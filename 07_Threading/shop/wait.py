import queue
from threading import Thread, Condition, Lock
from time import sleep, time

cv = Condition()
lock = Lock()

class Worker(Thread):
    def __init__(self, name, q):
        Thread.__init__(self)
        self.name = name
        self.flag = False
        self.ls = []
        self.start_time = time()
        self.q = q

    # class would take odd and even numbers from list

    def take_num(self):
        temp = self.q.get()
        self.q.put(temp)
        for num in temp:
            if (num / 100) / int(self.name) == 1:
                self.ls.append(num)
            if num == num * 100:
                self.flag
        with lock:
            print(f'numbers taken in :{time() - self.start_time}')

    def print_result(self):
        print(f'printed in :{time() - self.start_time}')
        print(self.ls)

    def run(self):
        self.take_num()
        print(self.q.empty())
        with cv:
            while self.q.empty():
                cv.wait()
        self.print_result()


def main():
    q = queue.Queue()
    workers = [Worker(i, q) for i in range(1, 11)]
    ls1 = [i for i in range(10000)]
    q.put(ls1)
    for worker in workers:
        worker.start()
    sleep(3)
    with cv:
        cv.notify_all()


if __name__ == '__main__':
    main()
