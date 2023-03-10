from turtle import Turtle


FONT = ("courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.create_scoreboard()
        self.update_scoreboard()

    def create_scoreboard(self):
        self.penup()
        self.hideturtle()
        self.color("black")
        self.goto(-200, 250)

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level:{self.level}", align="center", font=FONT)

    def level_up(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=FONT)
