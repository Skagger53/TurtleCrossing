if __name__ != "__main__": print("This is the main module. Do not call.")
else:
    import turtle as t
    import random
    import time as time
    import tkinter as tk
    from turtle import Screen
    from tkinter import messagebox as mb
    import therese as th
    from vehicles import Car
    from scorekeeper import Scorekeeper, give_answer
    from start_menu import starting_screen

    def setup_level(roads_crossed, lives_lost): # Setting up the level. Game doesn't start yet.
        stevie_the_scorekeeper.score_change(roads_crossed, lives_lost, 0, 0, difficulty)
        traffic = [] # List of all vehicles.

        lanes = [-140, -100, -60, -20, 60, 100, 140] # Lanes of traffic. Corresponds to the vertical movement of Therese. Includes a safety median with no vehicles.
        if difficulty > 2: lanes.append(20) # Removes the safety median if the difficulty is 3 or 4.
        start_x = -180 # Places first vehicle near the end of the screen and subsequent vehicles behind that.

        # Setting each lane's speed, based on difficulty. Here the min 2, max 10.
        speeds = {} # Lane speed is saved to this dictionary. Key is y-coordinate for that lane. Value is the speed. Used in Car.move()
        for speed in lanes: speeds[speed] = random.randint(2, difficulty * 2 + 4)

        # Places all vehicles initially.
        car_lines = 8 # How many cars are in each lane
        vehicle_length = None # Vehicle length is checked when creating a vehicle. Needed to keep vehicles from being drawn on top of each other. At the start of a level, it's always None, and initial creation will make 1, 2, or 3 segments. This variable is also used when creating a new car after another car has disappeared off the screen, and in that case, the old car's length is used for the new car's length.
        for next_cars in range(0, car_lines): # Creates vehicles in lanes. Creates first vehicle in all lanes, then second, etc.
            for traffic_lanes in lanes: # Creates vehicles in each lane
                moving_vehicle = Car(difficulty, start_x, traffic_lanes, vehicle_length)
                traffic.append(moving_vehicle) # Appends instance of Car class to "traffic" list
            start_x += 160 # Ensures that the next car won't be placed on top of the previous one

        return traffic, speeds # Returns the list of all cars as "traffic" and the dictionary of all lane speeds as "speeds".

    # Main game function and loop
    def main_game(roads_crossed, car_confrontations, traffic, speeds, answers):
        therese.setpos(0, -180)
        while has_chicken_answer == None:
            time.sleep(0.03) # Slowing down the game for the sake of the vehicles' speeds
            screen.update() # Keep things moving!

            def pause_game(): mb.showinfo("Paused", "Game paused.\n\nDon't keep Therese waiting too long!") # Pauses the game on spacebar press.

            def end_game(): # If the user presses "q", the game asks if they want to quit.
                if mb.askyesno("Quitting so soon?", "Do you want to quit without Therese discovering the mysteries of chickens and roads?"):
                    global has_chicken_answer
                    has_chicken_answer = False # Ends the current loop
                    if car_confrontations == 1: confrontation = "confrontation"  # Just adjusting the grammar for the message below
                    else: confrontation = "confrontations"
                    if roads_crossed == 1: roads = "road"
                    else: roads = "roads"
                    mb.showinfo("Having a Rest", f'Therese is done with road crossing...for now.\n\nJob well done!\n\nTherese crossed {roads_crossed} {roads} and had {car_confrontations} car "{confrontation}"!') # Ending message summarizing game score

            for i, vehicle in enumerate(traffic): # Vehicle AI. Moves vehicles until they go off the left side of the screen and deletes them and recreates a new one in the same lane off the right side of the screen. Also checks to see if Therese has been hit. Oh no!
                if vehicle.get_x() < -340: # checks to see if the vehicle is now off-screen and needs to be deleted and replaced with a new vehicle off of the right side of the screen.
                    y_coord = round(vehicle.get_y()) # Gets the y-coordinate (the lane) before deletion to create a new car in the same lane.
                    vehicle_length = len(vehicle.vehicle_segments) # When a vehicle is deleted after going off of the left side of the screen, its length is saved and used to generate the next car in the same lane off of the right side of the screen. Otherwise vehicles may be drawn on top of each other.
                    del vehicle # Deletes the unneeded instance of the vehicle class from memory
                    del traffic[i] # Deletes the now-unused index location of the deleted vehicle.
                    new_vehicle = Car(difficulty, 1000, y_coord, vehicle_length) # Creates a new vehicle off-screen.
                    traffic.append(new_vehicle) # Adds new vehicle to "traffic" list.
                else: # If vehicle is still on-screen.
                    vehicle.move(speeds) # Moves the vehicle. "speeds" is a dictionary. Key is each lane's y-coordinate. Value is each lane's previously determined random speed.
                    if round(therese.get_y()) == round(vehicle.vehicle_segments[0].ycor()): # Checking to see if Therese is in a lane of traffice. Watch out!
                        if round(therese.get_x()) > round(vehicle.vehicle_segments[0].xcor()) - 20 and round(therese.get_x()) < round(vehicle.vehicle_segments[-1].xcor()) + 20: # If Therese is in a lane of traffic, seeing if she's hitting or being hit by a car. The horror!
                            therese.setpos(0, -180) # Moves Therese back to the starting location when she is sadly struck by a vehicle. :'(
                            roads_crossed, car_confrontations = stevie_the_scorekeeper.score_change(roads_crossed, car_confrontations, 0, 1, difficulty)

            # All user input for Therese
            # Movement
            screen.onkeypress(lambda: therese.move_up() if therese.get_y() < 180 else None, "w")
            screen.onkeypress(lambda: therese.move_up() if therese.get_y() < 180 else None, "W")
            screen.onkeypress(lambda: therese.move_left() if therese.get_x() > -240 else None, "a")
            screen.onkeypress(lambda: therese.move_left() if therese.get_x() > -240 else None, "A")
            screen.onkeypress(lambda: therese.move_down() if therese.get_y() > -180 else None, "s")
            screen.onkeypress(lambda: therese.move_down() if therese.get_y() > -180 else None, "S")
            screen.onkeypress(lambda: therese.move_right() if therese.get_x() < 240 else None, "d")
            screen.onkeypress(lambda: therese.move_right() if therese.get_x() < 240 else None, "D")

            screen.onkeypress(pause_game, " ") # Pause

            # Quitting
            screen.onkeypress(end_game, "q")
            screen.onkeypress(end_game, "Q")

            if therese.get_y() >= 180: # When Therese reaches the other side of the road. Hooray!
                roads_crossed, car_confrontations = stevie_the_scorekeeper.score_change(roads_crossed, car_confrontations, 1, 0, difficulty)
                screen.update() # Ensures that the screen displays Therese's location safely out of traffic
                answer, answers = give_answer(answers) # Returns the randomized answer for this crossing and the list of answers with the answer currently being used removed
                if len(answers) != 0: # If there are still more answers (levels) left.
                    mb.showinfo("Road crossed!", f"Therese has successfully crossed the road!\n\nTherese has learned something new...\n\nShe learned that sometimes chickens cross the road {answer}")
                    return roads_crossed, car_confrontations, False # Returns the updated score and sets quit to False
                if car_confrontations == 1: confrontation = "confrontation" # Just adjusting the grammar for the message below
                else: confrontation = "confrontations"
                if car_confrontations == 0: mb.showinfo("Road crossed!", f'Therese has successfully crossed the road!\n\nTherese has learned something new...\n\nShe learned that sometimes chickens cross the road {answer}\n\nTherese has disovered all she can about chickens and roads. Job well done! Therese can now sleep at night and start each day well rested as she cares for those in need!\n\nTherese crossed {roads_crossed} roads and had {car_confrontations} car "{confrontation}"!\n\nWow! Way to keep Therese safe!')
                else: mb.showinfo("Road crossed!", f'Therese has successfully crossed the road!\n\nTherese has learned something new...\n\nShe learned that sometimes chickens cross the road {answer}\n\nTherese has disovered all she can about chickens and roads. Job well done! Therese can now sleep at night and start each day well rested as she cares for those in need!\n\nTherese crossed {roads_crossed} roads and had {car_confrontations} car "{confrontation}"!')
                return roads_crossed, car_confrontations, True # Returns final score (though this isn't actually used) and sets quit to True

        return roads_crossed, car_confrontations, True

    # The game variables and setup begins here
    answers = ["just to get to the other side.", "because they're in a fowl mood.", "just beak-cause they can!",
               "because they think it's an egg-cellent idea.", "to boldly go where no chicken has gone before.",
               "to get away from Colonel Sanders.", "to warn people that the sky is falling.",
               "to get away from people who keep asking them why they cross roads!", "to get to New Yolk City.",
               "to see the latest chick flick."] # List of possible answers that Therese can discover!

    difficulty = 5 # Sets the difficulty level to 5, which is the Quit option in starting_screen(). This way if the user simply closes out the window of the starting screen without making a selection, the game will properly close by defaulting to the Quit option.
    difficulty = starting_screen(difficulty) # Setting the game difficulty. Options are 0, 1, 3, 4 (2 was originally going to be an option but I changed my mind)

    screen = Screen()
    screen.setup(550, 400)
    screen.title("Of Turtles and Chickens")
    screen.tracer(0)  # Stops the screen from updating. Screen only updates once per loop

    stevie_the_scorekeeper = Scorekeeper() # Sets up the scoring system in the corner of the screen.
    roads_crossed, lives_lost = 0, 0 # Sets initial score

    screen.listen()

    therese = th.TheTurtle()  # The player's turtle
    has_chicken_answer = None  # Therese's sad initial state...not knowing the crucial answer!

    if difficulty != 5: quit = False # If starting_screen() returns 5, the user clicked "Quit"
    while quit == False:
        traffic, speeds = setup_level(roads_crossed, lives_lost) # Initial setup screen/game intro. Returns all car classes in "traffic" list and a dictionary of all randomly selected lane speeds.
        roads_crossed, lives_lost, quit = main_game(roads_crossed, lives_lost, traffic, speeds, answers) # Starts the game running. Each time a level is completed, the score for roads crossed and car confrontations is returned along with quit as False or True to continue or stop playing.
        for vehicle in traffic: # Removes turtles from being visible on the screen and deletes them from memory. They are recreated from scratch at the start of each new level. This allows for variety in lane speeds and the order of vehicles (by their length)
            for segment in vehicle.vehicle_segments:
                segment.hideturtle()
                del segment