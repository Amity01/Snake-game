from turtle import Turtle

Alignment = "center"
Font = ("Courier", 24, "normal")
Color = "white"


class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.hideturtle()
        with open("high_score.txt") as data:
            self.high_score = int(data.read())
        self.score = 0
        self.color(Color)
        self.penup()
        self.goto(-100, 260)
        self.update_Scoreboard()

    def update_Scoreboard(self):
        self.clear()
        self.goto(-100, 260)
        self.write(f"Score: {self.score}", align=Alignment, font=Font)
        self.goto(100, 260)
        self.write(f"HighScore: {self.high_score}", align=Alignment, font=Font)

    def reset(self):
        if self.high_score < self.score:
            self.high_score = self.score
        self.score = 0
        with open("high_score.txt","w") as data:
            data.write(f"{self.high_score}")
        self.update_Scoreboard()

    def increment_score(self):
        self.score += 1
        self.clear()
        self.update_Scoreboard()
