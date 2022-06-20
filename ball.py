from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 5
        self.y_move = 5
        self.move_speed = 0.1
        # self.home()=> origin coordinates of turtle

    def move(self):
        new_x = self.xcor() + self.x_move # .xcor() returns the turtle’s x coordinate where it was for last time on axis "x"
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1
        # self.move_speed *= 0.5

    # to avoid multiple bounces => functions for colisition with paddles separately to change the direction when still within the 50 pixels range
    def bounce_x_r_paddle(self):
        self.x_move = (-abs(self.x_move))
        self.move_speed *= 0.85

    def bounce_x_l_paddle(self):
        self.x_move = abs(self.x_move)
        self.move_speed *= 0.85

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        #self.bounce_x()
