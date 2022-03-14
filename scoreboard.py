from turtle import Turtle

ALIGNMENT = "center"
FONT = ("courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(x=0, y=270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f" Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self, name):
        self.goto(x=0, y=0)
        self.write(f"GAME OVER {name}\nScore farany: {self.score}", align=ALIGNMENT, font=FONT)

    def score_up(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
