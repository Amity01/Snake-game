from turtle import Turtle

Alignment = "center"
Font = ("Courier", 24, "normal")
Color = "white"


class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.hideturtle()
        self.score = 0
        self.color(Color)
        self.penup()
        self.goto(0, 260)
        self.update_Scoreboard()

    def update_Scoreboard(self):
        self.write(f"Score: {self.score}", align=Alignment, font=Font)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=Alignment, font=Font)

    def increment_score(self):
        self.score += 1
        self.clear()
        self.update_Scoreboard()
