class Node:
    def __init__(self, indata):
        self.data = indata
        self.next = None

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext

    def getData(self):
        return self.data

    def getNext(self):
        return self.next
