from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=6)
        self.setheading(90)
        self.set_paddle_pos(pos)

    def set_paddle_pos(self, pos):
        self.goto(pos)

    def move_up(self):
        self.forward(10)

    def move_down(self):
        self.backward(10)
