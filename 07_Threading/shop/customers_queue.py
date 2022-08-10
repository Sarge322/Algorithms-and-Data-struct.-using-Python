class Queue:
    def __init__(self):
        # list of current customers in queue
        self.customers = []
        # if 10 or more customers
        self.overloaded = False

    def enqueue(self, customer):
        self.customers.append(customer)

    def dequeue(self):
        self.customers.pop(0)

    def queue_size(self):
        return len(self.customers)

