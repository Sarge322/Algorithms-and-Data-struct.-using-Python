from node import Node


class UnorderedList:
    def __init__(self):
        self.head = None
        self.last = None

    def isEmpty(self):
        return self.head is None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
        if self.last is None:
            self.last = temp

    def append(self, item):
        temp = Node(item)
        self.last.setNext(temp)
        self.last = temp

    def insert(self, item, pos):
        temp = Node(item)
        current = self.head
        previous = None
        ind = 0
        while pos != 0:
            if ind > 0:
                previous = current
                current = current.getNext()
            elif current.getNext() is None:
                previous = current
            if ind == pos:
                break
            ind = ind + 1
        if pos != 0:
            if previous is not None:
                previous.setNext(temp)
            temp.setNext(current)
        else:
            temp.setNext(self.head)
            self.head = temp

    def size(self):
        current = self.head
        count = 0

        while current is not None:
            count = count + 1
            current = current.getNext()

        return count

    def search(self, item):
        current = self.head
        found = False

        while current is not None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

    def index(self, item):
        current = self.head
        index = 0
        found = True

        while current is not None:

            if current.getData() == item:
                found = True
                break
            current = current.getNext()
            index = index + 1

        return index if found else None

    def pop(self):
        current = self.head
        previous = None

        while current.getNext() is not None:
            previous = current
            self.last = previous
            current = current.getNext()
        previous.setNext(None)

        return current.getData()

    def remove(self, item):
        current = self.head
        previous = None
        found = False

        while not found and current is not None:
            if current.getData() == item:
                found = True
                break
            else:
                previous = current
                current = current.getNext()

        if found and current.getNext() is None:
            if previous is None:
                self.last = previous
            else:
                self.head = None
                self.last = None
        elif found and previous == None:
            if current.getNext != None:
                self.head = current.getNext()

            else:
                self.head = None
        else:
            previous.setNext(current.getNext())

    def print_u_list(self):
        current = self.head
        result = ''
        while True:
            result = result + str(current.getData()) + " "
            if current.getNext() == None:
                break
            current = current.getNext()
        return result


def test_U_list():
    u = UnorderedList()
    u.add(1)
    u.add(2)
    u.add(3)
    u.add(4)
    # res = u.search(99)
    # assert res == False, f"Error, False res: {res}"
    # res = u.search(3)
    # assert res == True, f"Error, True res: {res}"
    print(u.print_u_list())
    u.insert(911, 3)
    print(u.print_u_list())
    print(u.index(1))
    print(u.print_u_list())
    print(u.pop())
    print(u.pop())
    print(u.pop())
    u.append(9)
    print(u.print_u_list())
    # assert res == 3, f"Error, 1 res: {res}"
    # print(u.print_u_list())
    print("Well done!!!!")


if __name__ == "__main__":
    test_U_list()
