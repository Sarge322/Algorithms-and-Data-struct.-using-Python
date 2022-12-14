import turtle


def fractal_helix(length, t):
    while length > 10:
        t.right(3)
        t.forward(length // 4-1)
        t.right(3)
        t.right(3)
        t.forward(length // 4 - 1)
        t.right(3)
        t.right(3)
        t.forward(length // 4 - 1)
        t.right(3)

        fractal_helix(length - 1, t)


def main():
    t = turtle.Turtle()
    my_win = turtle.Screen()
    t.color('red')
    fractal_helix(100, t)
    t.speed(0)
    my_win.exitonclick()


main()
