from turtle import Turtle

MOVE_DISTANCE = 20

class Snake:
    def __init__(self):
        self.head = Turtle()
        self.head.color('#03fcf4')
        self.head.shape('square')
        self.head.speed(1)
        self.head.pu()
        self.elements = []
        self.elements.append(self.head)

    def move_up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def move_left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def move_down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def move_right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def move(self):
        # Tutaj od końca każdy element przeskakuje na miejsce następnego, a głowa robi ostatni ruch
        for element_index in range(len(self.elements) - 1, 0, -1 ):
            new_x = self.elements[element_index-1].xcor()
            new_y = self.elements[element_index-1].ycor()
            self.elements[element_index].goto(new_x,new_y)
        self.head.fd(MOVE_DISTANCE)

    def restart_position(self):
        self.head.goto(x=0, y=0)

    def new_segment(self):
        new_segment = Turtle()
        new_segment.color('#03fcf4')
        new_segment.shape('square')
        new_segment.pu()
        self.elements.append(new_segment)


    def reset(self):
        for element in self.elements:
            element.goto(0,0)
            element.hideturtle()


        self.elements.clear()
        self.head = Turtle()
        self.head.color('#03fcf4')
        self.head.shape('square')
        self.head.speed(1)
        self.head.pu()
        self.elements.append(self.head)

