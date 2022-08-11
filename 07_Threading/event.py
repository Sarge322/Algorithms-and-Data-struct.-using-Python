from random import randrange
from threading import Thread, Event, Condition
from time import sleep, time

event = Event()
cv = Condition()


def worker(name: str):
    time1 = time()
    event.wait()
    with cv:

        print(f"Worker: {name}, time:{time() - time1}")


workers = [Thread(target=worker, args=(f"wrk {i}",)) for i in range(10)]

for w in workers:
    w.start()

print("Main thread")

event.set()
