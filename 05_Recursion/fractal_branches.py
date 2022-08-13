import turtle
from random import randrange


def tree(branch_len, t):
    dist = randrange(6, 22)
    if branch_len > 5:
        if branch_len <= dist:
            t.color('green')
        if branch_len >= 30:
            x = randrange(15, 45)
            if x%2 is not 0:
                x = x + 1
        else:
            x = 40
        t.pensize(branch_len/15)
        t.forward(branch_len)
        t.right(x/2)
        tree(branch_len - dist, t)
        t.left(x)
        tree(branch_len - dist, t)
        t.right(x/2)
        if branch_len > dist:
            t.color('brown')
        t.backward(branch_len)


def main():
    t = turtle.Turtle()
    my_win = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(400)
    t.down()
    t.color('brown')
    tree(150, t)
    t.speed(0)

    my_win.exitonclick()


main()
