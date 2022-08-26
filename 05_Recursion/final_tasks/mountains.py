import turtle


def mountains(points, color, my_turtle):
    my_turtle.fillcolor(color)
    my_turtle.up()
    my_turtle.goto(points[0][0], points[0][1])
    my_turtle.down()
    my_turtle.begin_fill()
    my_turtle.goto(points[1][0], points[1][1])
    my_turtle.goto(points[2][0], points[2][1])
    my_turtle.goto(points[0][0], points[0][1])
    my_turtle.end_fill()


def get_mid(p1, p2):
    return (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2


def sierpinsky(points, degree, my_turtle):
    colormap = ['blue', 'red', 'green', 'white', 'yellow', 'violet', 'orange']
    mountains(points, colormap[degree], my_turtle)
    if degree > 0:
        sierpinsky([points[0],
                    get_mid(points[0], points[1]),
                    get_mid(points[0], points[2])],
                    degree-1, my_turtle)
        sierpinsky([points[1],
                    get_mid(points[0], points[1]),
                    get_mid(points[1], points[2])],
                    degree-1, my_turtle)
        sierpinsky([points[2],
                    get_mid(points[2], points[1]),
                    get_mid(points[0], points[2])],
                    degree-1, my_turtle)


def main():
    my_turtle = turtle.Turtle()
    my_win = turtle.Screen()
    my_points = [[-100, -50], [0, 100], [100, -50]]
    sierpinsky(my_points, 5, my_turtle)
    my_win.exitonclick()


if __name__ == '__main__':
    main()