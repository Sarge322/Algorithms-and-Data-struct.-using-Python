import turtle


# drawing simple square with given length of side and fill it with color
def draw_square(length, color, my_turtle):
    my_turtle.fillcolor(color)
    my_turtle.begin_fill()
    for i in range(4):
        my_turtle.forward(length)
        my_turtle.left(90)
    my_turtle.end_fill()


def draw_inner_square(length, deepth, my_turtle):
    # set some color list
    color_map = ['red', 'yellow', 'green', 'brown', 'white', 'purple']
    # drawing initial square
    draw_square(length, color_map[deepth], my_turtle)
    # draw 4 square in
    if deepth > 0:
        # each square will be separate from each other on 10% length of side previous square side
        margin_length = length * 0.45
        draw_inner_square(
            margin_length, deepth - 1, my_turtle
        )
        # set initial position for drawing of next square
        my_turtle.forward(length * 0.55)
        draw_inner_square(
            margin_length, deepth - 1, my_turtle
        )
        # -//-
        my_turtle.forward(margin_length)
        my_turtle.left(90)
        my_turtle.forward(length * 0.55)
        draw_inner_square(
            margin_length, deepth - 1, my_turtle
        )
        # -//-
        my_turtle.forward(margin_length)
        my_turtle.left(90)
        my_turtle.forward(length * 0.55)
        draw_inner_square(
            margin_length, deepth - 1, my_turtle
        )
        # set cursor for
        my_turtle.forward(margin_length)
        my_turtle.left(90)
        my_turtle.forward(length)
        my_turtle.left(90)


def main():
    # create instance of Turtle class
    my_turtle = turtle.Turtle()
    # create screen
    my_win = turtle.Screen()
    my_win.bgcolor('light green')
    my_win.title('Square of squares')
    my_turtle.speed(0)
    # set length of square side
    side_length = 300
    # set depth of 'square in square' recursion
    depth = 3
    draw_inner_square(side_length, depth, my_turtle)
    my_win.exitonclick()


if __name__ == '__main__':
    main()
