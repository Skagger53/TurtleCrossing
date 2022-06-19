if __name__ == "__main__": print("This is a supporting file. Do not execute directly.")
else:
    from turtle import Turtle

    # The class for our heroine Therese!
    class TheTurtle(Turtle):
        def __init__(self):
            super().__init__()
            self.shape("turtle")
            self.penup()
            self.hideturtle()
            self.color("purple")
            self.seth(90)
            self.showturtle()

        # All user input for Therese
        def move_up(self): self.forward(40)
        def move_down(self): self.backward(40)
        def move_left(self): self.setpos(self.xcor() - 20, self.ycor())
        def move_right(self): self.setpos(self.xcor() + 20, self.ycor())

        # Returning Therese's x-coordinate and y-coordinate values
        def get_x(self): return self.xcor()
        def get_y(self): return self.ycor()