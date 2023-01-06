from turtle import Turtle

# constans
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]

MOVE_DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGTH = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("aquamarine")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):#debems traer la ultima oposicion en donde se encuentra el cuerpo de la culebra
        #pñosuition metodo que indica la posicion
        self.add_segment(self.segments[-1].position())

    def move(self):
        # position body snake -> reverse
        for seg_num in range(len(self.segments) - 1, 0, -1):
            # neceasrio para colocar la parte de la cola ahi luego
            # they are parts of the snake -> its the secon part --> (o, X, o )
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            # (o,x,o) -> new position in the screen
            self.segments[seg_num].goto(new_x, new_y)  # (none,o,x)
        self.head.forward(MOVE_DISTANCE)

    # cuidado con eso de que se de media vuelta entre si
    def up(self):
        # return the direction of cabeza culebrea
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGTH:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGTH)
