from stack import Stack


def hanoi(n, first, last):
    if n <= 0:
        return
    temp = 6 - first - last
    hanoi(n - 1, first, temp)
    print(f'move {n} from {first} to {last}')
    hanoi(n - 1, temp, last)


def move_disc(num, start, finish, mid):
    if num <= 0:
        return
    move_disc(num - 1, start, mid, finish)
    disc = start.pop()
    finish.push(disc)
    print('{:2d} {:7}{:8s}{:7s}{:8s}{:7s}{:8s}'.format(num, start.name, str(start.show()), mid.name,
                                                       str(mid.show()), finish.name, str(finish.show())))
    move_disc(num - 1, mid, finish, start)


def main():
    # first_tower = Stack()
    # first_tower.setName('First')
    # for i in range(3, 0, -1):
    #     first_tower.push(i)
    # second_tower = Stack()
    # second_tower.setName('Second')
    # third_tower = Stack()
    # third_tower.setName('Third')
    # print(
    #     f"{first_tower.name, first_tower.show()}----{second_tower.name, second_tower.show()}----{third_tower.name, third_tower.show()}")
    #
    # move_disc(3, first_tower, third_tower, second_tower)
    # move_disc(3, 1, 3, 2)
    hanoi(3, 1, 3)

if __name__ == '__main__':
    main()

