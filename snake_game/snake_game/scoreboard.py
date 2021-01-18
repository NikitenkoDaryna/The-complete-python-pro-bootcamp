from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_number = 0
        self.hideturtle()
        self.color("white")
        self.penup()

    def write_score_number(self):
        self.setposition(0, 265)
        self.write(f"Score: {self.score_number}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
