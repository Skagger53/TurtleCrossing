if __name__ == "__main__": print("This is a supporting file. Do not execute directly.")
else:
    import random
    from turtle import Turtle

    class Car(Turtle):
        def __init__(self, difficulty, start_x, start_y, vehicle_length):
            colors = ("aquamarine", "bisque3", "black", "blue", "brown2", "cyan", "DarkBlue", "DeepPink", "LightGoldenrod4", "LightSeaGreen", "maroon1", "peru", "plum1", "SteelBlue3", "YellowGreen") # Possible vehicle colors
            vehicle_offset = (-10, 0, 10) # Possible distance between vehicles
            start_x = start_x + random.choice(vehicle_offset) # Adjusts the start location slightly for a little variety. Shouldn't cause vehicles to overlap because the initial start_x is static.

            self.vehicle_segments = [] # Each vehicle is a list of a random number (1 to 3) of turtles (segments). When I wrote this code, I did not know about the stretch-wid attribute. That would have been a much simpler solution than this.
            car_color = random.choice(colors) # Color is random
            if vehicle_length == None: vehicle_length = random.randint(1, 3) # Sets the length of this instance of the vehicle. 1 to 3 segments/turtles of 20 pixels each. Again, using stretch-wid would have been better, but I didn't know about that attribute.
            for i, segment in enumerate(range(vehicle_length)):
                segment = Turtle()
                segment.color(car_color)
                segment.shape("square")
                segment.penup()
                segment.seth(180) # This isn't stricly needed but allows the vehicles to use the "forward" method to go forward. (Default heading would require "backward" method, which would work but I don't prefer.)
                segment.setpos(start_x + i * 20, start_y) # Sets the position of the vehicle off-screen. Each segment is offset by 20 pixels.
                self.vehicle_segments.append(segment) # Adds in each new segment to the full vehicle

        def move(self, speed_dict): # Moves the vehicle at the speed determined by the speed_dict dictionary. Key is the y-value of the car (the lane). Value is the speed.
            for segment in self.vehicle_segments: segment.forward(speed_dict[round(segment.ycor())]) # Rounds in the case of an accidental floating point y coordinate. Moves each segment one after the other. Using the stretch-wid attribute for vehicles instead of these segments in a list would have been better, but I didn't know about that attribute when I wrote this.

        def get_x(self): return self.vehicle_segments[0].xcor() # Returns vehicle's x coordinate of its first (front) segment

        def get_y(self): return self.vehicle_segments[0].ycor() # Returns vehicle's y coordinate of its first (front) segment