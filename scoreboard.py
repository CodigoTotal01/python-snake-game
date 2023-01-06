import turtle
from turtle import Turtle
#values constants

ALINE = "center"
FONT = ("Victor Mono", 20, "normal")
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALINE, font=FONT )

    def increase_score(self):
        self.score +=1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER 🐍", align=ALINE, font=FONT)