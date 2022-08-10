from node import Node


class OrderedList:
    def __init__(self):
        self.head = None
        self.last = None

    def isEmpty(self):
        return self.head is None

    def size(self):
        current = self.head
        count = 1
        while True:
            if current.getNext():
                count = count + 1
                current = current.getNext()
            else:
                break
        return count

    def print(self):
        current = self.head
        res = ''
        if current is not None:
            while current is not None:
                res = res + str(current.getData())
                if current.getNext() is None:
                    break
                res = res + ', '
                current = current.getNext()

        return res

    def add(self, item):
        current = self.head
        prev = None
        temp = Node(item)

        while True:
            # check for empty list and just add 1st number
            if self.head is None:
                self.head = temp
                self.last = temp
                break
            # check for 'item' stand before current position in list
            if item <= current.getData():
                if prev is None:
                    self.head = temp
                    temp.setNext(current)
                # check if pos in the middle
                elif prev is not None and current.getNext() is not None or current.getNext() is None:
                    prev.setNext(temp)
                    temp.setNext(current)
                break
            # check if 'item' bigger than biggest num in list
            elif item > current.getData() and current.getNext() is None:
                current.setNext(temp)
                self.last = temp
                break
            # sort through list looking for 'if' statement above
            if current.getNext() is not None:
                prev = current
                current = current.getNext()

    def index(self, item):
        current = self.head
        index = 0
        found = False

        while current is not None:
            if current.getData() == item:
                found = True
                break
            elif current.getData() >= item and not found:
                print(index)
                break
            else:
                current = current.getNext()
                index = index + 1

        return index if found else None

    def search(self, item):
        current = self.head
        found = False

        while current is not None:
            if current.getData() == item:
                found = True
                break
            elif current.getData() >= item and not found:
                break
            else:
                current = current.getNext()

        return found

    def pop(self):
        current = self.head
        prev = None
        if current is not None:
            if current is not None and current.getNext() is not None:
                while current.getNext() is not None:
                    prev = current
                    current = current.getNext()
                prev.setNext(None)
            else:
                self.head = None

        return None if current is None else current.getData()

    def remove(self, item):
        current = self.head
        prev = None

        if current is not None:
            while current is not None:
                if current.getData() == item:
                    if prev is None and current.getNext() is None:
                        self.head = None
                    elif prev is None and current.getNext() is not None:
                        self.head = current.getNext()
                        current.setNext(None)
                    else:
                        prev.setNext(current.getNext())
                    break
                if current.getNext() is not None:
                    prev = current
                    current = current.getNext()



def test_ordered_list():
    o = OrderedList()
    print(o.isEmpty())
    o.add(4)
    o.add(65)
    print(o.print())

    print(str(o.print()))

    print(o.search(100))
    o.add(122)

    print(o.pop())
    print(str(o.print()))

    o.remove(65)
    print(str(o.print()))
    print('________________________')

    o.remove(4)
    print(str(o.print()))
    o.remove(4)
    print(str(o.print()))

    # o.remove(228)
    # print(str(o.print()))


if __name__ == "__main__":
    test_ordered_list()
