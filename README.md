# TurtleCrossing
Therese the Turtle road crossing to answer that age-old question...

Has only one real dependency that requires installation: PIL (ImageTk, Image)

Place all files in the same directory, install Pillow, and run main.py.

One approach I wish I'd changed was how I build the vehicles in this. I took individual 20 x 20 turtles and, if a vehicle was 2 or 3 "lengths" long (40 x 20 or 60 x 20), I placed several turtles beside each other and move them along. I probably would've done better to use the stretch-wid attribute for a single turtle for this, though then this would've been trickier to detect collisions, but I could've figured something out.
