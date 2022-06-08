from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.high_score = 0
        self.score = 0
        self.hideturtle()
        self.pu()
        self.color("white")
        self.goto(0,270)


    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0

    def printing_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}" , move=False, align="center", font=('Arial', 20, "normal"))


