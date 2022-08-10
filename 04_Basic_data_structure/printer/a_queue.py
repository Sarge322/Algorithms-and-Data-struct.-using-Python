class Queues:
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



