from threading import Thread, Lock, RLock
from random import randint, randrange

from time import sleep
import queue


# shelf with baskets
class Shelf:
    # creating list of baskets
    def __init__(self):
        self.basket_shelf = []

    # fill shelf with empty baskets
    def add_baskets(self):
        for i in range(20):
            self.basket_shelf.append(Basket(i))


class Basket:
    def __init__(self, name):
        self.name = name
        self.goods = 0

    def fill(self, q):
        self.goods = self.goods + q
        print(f'Basket {self.name} got {self.goods} goods, q = {q}')


class Worker(Thread):
    lock = RLock()

    def __init__(self, name, q):
        Thread.__init__(self)
        self.name = name
        self.q = q
        self.basket = None

    def take_basket(self):

        try:
            sleep(randrange(2))
            shelf = self.q.get()
            self.basket = shelf.basket_shelf.pop()
            self.q.put(shelf)
            with self.lock:
                print(f'Worker {self.name} got basket {self.basket.name}')
        except Exception:
            pass

    def sleep_timer(self):
        sleep(randrange(1))

    def leave_basket(self):
        try:
            shelf = self.q.get()
            shelf.basket_shelf.append(self.basket)
            self.q.put(shelf)
            with self.lock:
                print(f'{self.name} worker put basket {self.basket.name} in the queue')
            self.basket = None
        except Exception:
            print(Exception)

    def add_goods(self):
        for i in range(randrange(1, 2)):
            self.basket.fill(randrange(1, 3))

    def run(self):
        self.take_basket()
        self.sleep_timer()
        self.add_goods()
        # self.leave_basket()


def main():
    q = queue.Queue()
    workers = []
    shelf = Shelf()
    shelf.add_baskets()
    q.put(shelf)

    for i in range(18):
        workers.append(Worker(i, q))
    for worker in workers:
        worker.start()
    for w in workers:
        w.join()
    for basket in q.get().basket_shelf:
        print(f'basket {basket.name} has {basket.goods} number')

    sleep(1)

    cashier_q = 1

    def check_queue(self):
        if queue.size() < 10:
            pass


if __name__ == '__main__':
    main()
