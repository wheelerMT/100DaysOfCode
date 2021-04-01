from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        # Set up scoreboard turtle
        super().__init__()
        self.ht()
        self.color("white")
        self.pu()
        self.goto((0, 270))

        # Write the initial score
        self.score = 0
        self.write_score()

    def write_score(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto((0, 0))
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increment_score(self):
        self.score += 1
        self.clear()
        self.write_score()
