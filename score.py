from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 16, "normal")

'''Creates score by inheriting from turtle classes '''


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open( "data.txt" ) as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=270)
        self.update_score()

    '''Updates score without overlay'''

    def update_score(self):
        self.clear()
        self.write(f"Score:{self.score} | High score:{self.high_score}", align=ALIGNMENT, font=FONT)

    '''Shows GAME OVER method when snake hits tail or wall'''

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt" ,mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_score()
    '''Increases score by 1 each time when snake heats food'''

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()
