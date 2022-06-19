if __name__ == "__main__": print("This is a supporting file. Do not execute directly.")
else:
    from turtle import Turtle

    # Draws all sidewalks
    def draw_sidewalks(difficulty): # Difficulty is 0, 1, 3, 4. The highest two difficulties do not have the safety median in the middle.
        y_coords = [-180, 180]
        if difficulty < 3: y_coords.append(20) # Adds the safety median for easier difficulties
        manny_the_mason = Turtle()
        manny_the_mason.hideturtle()
        manny_the_mason.shape("square")
        manny_the_mason.penup()
        manny_the_mason.color("gray80")
        manny_the_mason.width(25)
        for sidewalk in y_coords: # Draws the sidewalks from the coordinates -- 3 including median for easier modes, only two for harder.
            manny_the_mason.goto(-275, sidewalk)
            manny_the_mason.pendown()
            manny_the_mason.goto(275, sidewalk)
            manny_the_mason.penup()