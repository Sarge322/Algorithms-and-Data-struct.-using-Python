import random


class Queue:
    def __init__(self):
        self.q = []

    def enqueue(self, item):
        self.q.insert(0, item)

    def dequeue(self):
        return self.q.pop()

    def isEmpty(self):
        return self.q == []

    def size(self):
        return len(self.q)


def hot_potato(players):
    que = Queue()

    for i in players:
        que.enqueue(i)

    while que.size() > 1:
        temp = que.dequeue()
        if random.randrange(0, 6) == 2:
            print(temp, " leave")
            continue
        else:
            que.enqueue(temp)
            print("pass")
    return que.dequeue()

hot_potato(['a', 'b', 'c'])
