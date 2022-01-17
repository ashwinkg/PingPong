from turtle import Turtle

FONT_STYLE = ('Arial', 20, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.print_score_board()

    def print_score_board(self):
        self.clear()
        self.goto(100, 370)
        self.write(arg=f"{self.right_score}", align="center", font=FONT_STYLE)
        self.goto(-100, 370)
        self.write(arg=f"{self.left_score}", align="center", font=FONT_STYLE)

    def update_left_score(self):
        self.left_score += 1

    def update_right_score(self):
        self.right_score += 1
