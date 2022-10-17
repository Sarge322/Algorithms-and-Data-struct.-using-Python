from threading import Thread, BoundedSemaphore, Condition
from time import sleep, time

ticket_office = BoundedSemaphore(value=3)
cv = Condition()

def ticket_buyer(number):
    start_service = time()
    with ticket_office:
        sleep(1)
        with cv:
            print(f"client {number}, service time: {time() - start_service}")


buyer = [Thread(target=ticket_buyer, args=(i,)) for i in range(5)]

for j in buyer:
    j.start()
