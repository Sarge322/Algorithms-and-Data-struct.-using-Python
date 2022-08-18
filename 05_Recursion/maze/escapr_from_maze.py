import turtle

PART_OF_PATCH = '0'
TRIED = '.'
OBSTACLE = '+'
DEAD_END = '-'


class Maze:
    def __init__(self, maze_map):
        rows_in_maze = 0
        cols_in_maze = 0
        self.maze_list = []
        maze_file = open(maze_map, 'r')

        for line in maze_file:
            rows_list = []
            col = 0
            for ch in line[:-1]:
                rows_list.append(ch)
                if ch == 'S':
                    self.startRow = rows_in_maze
                    self.startCol = col
                col = col + 1
            rows_in_maze = rows_in_maze + 1
            self.maze_list.append(rows_list)
            cols_in_maze = len(rows_list)

        self.rows_in_maze = rows_in_maze
        self.cols_in_maze = cols_in_maze
        self.x_translate = -cols_in_maze / 2
        self.y_translate = rows_in_maze / 2
        self.t = turtle.Turtle()
        self.t.shape('turtle')
        self.win = turtle.Screen()

        self.win.setworldcoordinates(-(cols_in_maze - 1) /
                                    2 - .5, -(rows_in_maze - 1) /
                                    2 - .5, (cols_in_maze - 1) /
                                    2 + .5, (rows_in_maze - 1) / 2 + .5)

    def draw_maze(self):
        self.t.speed(0)
        for y in range(self.rows_in_maze):
            for x in range(self.cols_in_maze):
                if self.maze_list[y][x] == OBSTACLE:
                    self.draw_centered_box(x + self.x_translate, -y + self.y_translate, 'orange')
        self.t.color('brack')
        self.t.fillcolor('blue')

    def draw_centered_box(self, x, y, color):
        self.t.up()
        self.t.goto(x - .5, y - .5)
        self.t.color(color)
        self.t.fillcolor(color)
        self.t.setheading(90)
        self.t.down()
        self.t.begin_fill()
        for i in range(4):
            self.t.forward(1)
            self.t.right(90)
        self.t.end_fill()


maze = Maze('maze_map.txt')
maze.draw_maze()
