from shop.bucket_shelf import BasketShelf
from shop.customer import Customer
import threading
import time
import random
from shop.util import file_reader

in_shop = 4
customers = []


def create_customers(num):
    names = file_reader('customer_names.txt')
    while num >= 0:
        time.sleep(1)
        temp = Customer()
        temp.setName(names[random.randrange(0, len(names) - 1)])
        customers.append(temp)
        num = num - 1
        print(temp.getName(), 'enter')


def leave():
    time.sleep(1)
    if len(customers) > 0:
        print(customers.pop(0).getName(), 'leave')
    time.sleep(2)


for i in range(60):
    create_customers(4)
    leave()