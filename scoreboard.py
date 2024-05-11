from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self, position) -> None:
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(position)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.write(self.score, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()