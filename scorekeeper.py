if __name__ == "__main__": print("This is a supporting file. Do not execute directly.")
else:
    import random
    from turtle import Turtle
    from sidewalks import draw_sidewalks

    class Scorekeeper(Turtle): # The scorekeeping turtle. Keeps track of roads crossed and car confrontations.
        def __init__(self):
            self.scoring_turtle = Turtle()
            self.scoring_turtle.hideturtle()
            self.scoring_turtle.color("black")
            self.scoring_turtle.penup()
            self.scoring_turtle.setpos(15, 172)
            self.scoring_turtle.write("Roads crossed: 0 Car confrontations: 0", font = ("Arial", 10, "bold"))

        def score_change(self, roads_crossed, car_confrontations, new_roads_crossed, new_car_confrontations, difficulty): # Updates the score. Arguments are current scores and changes to the score.
            roads_crossed += new_roads_crossed
            car_confrontations += new_car_confrontations
            draw_sidewalks(difficulty) # Draws sidewalks, including median for easier difficulties.
            self.scoring_turtle.write(f"Roads crossed: {roads_crossed} Car confrontations: {car_confrontations}", font=("Arial", 10, "bold")) # Writes the new score.
            return roads_crossed, car_confrontations # Returns the updated score

    def give_answer(answers): # Upon reaching the other side (three cheers!), the scorekeeper imparts his wisdom to Therese and tells her a little about why chickens cross roads. Argument is the full list of answers.
        answer = answers.pop(random.randint(0, len(answers) - 1)) # Getting the answer and removing it from the full answers list.
        return answer, answers # Returns the answer for this level and the updated "answers" list.