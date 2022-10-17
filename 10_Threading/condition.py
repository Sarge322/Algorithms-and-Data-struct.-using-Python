from queue import Queue
from threading import Condition, Thread
from time import sleep

cv = Condition()
q = Queue()


def order_processor(name):
    while True:
        with cv:
            while q.empty():
                cv.wait()

            try:
                order = q.get_nowait()
                print(f'{name}: {order}')

                if order == 'stop':
                    break

            except:
                pass
            sleep(1)


tr = [Thread(target=order_processor, args=(f'thread {i}',)) for i in range(1, 4)]

for t in tr:
    print(t)
    t.start()
for i in range(10):
    q.put(f'order {i}')

for j in range(3):
    q.put('stop')

with cv:
    cv.notify()
