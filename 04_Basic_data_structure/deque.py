class Deque:
    def __init__(self):
        self.que = []

    def addFront(self, item):
        self.que.append(item)

    def addRear(self, item):
        self.que.insert(0, item)

    def removeFront(self):
        return self.que.pop()

    def removeRear(self):
        return self.que.pop(0)

    def isEmpty(self):
        return self.que == []

    def size(self):
        return len(self.que)


def palindrom_check(word):
    q = Deque()
    for let in word:
        q.addRear(let)

    while q.size() > 1:
        if q.removeRear() != q.removeFront():
            return False
        else:
            return 'palindrom'

ls = ['toot', 'madam', 'radar', 'dog']
for i in ls:
    print(i, palindrom_check(i))
