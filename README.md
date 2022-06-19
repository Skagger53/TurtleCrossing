# TurtleCrossing
Therese the Turtle crossing the road to answer that age-old question...

Has only one real dependency that requires installation: PIL (ImageTk, Image)

Place all files in the same directory, install Pillow, and run main.py.

During the game, press spacebar to pause. Press "q" to quit.

Easy and normal modes have a median in the middle of the road where no vehicles will appear. The car speeds increase as the difficulty goes up.

One approach I wish I'd changed was how I build the vehicles in this. I took individual 20 x 20 turtles and had vehicles one to three "lengths" (20 x 20, 40 x 20, 60 x 20). For two- or three-length vehicles, I placed several turtles beside each other and move them uniformly. I probably would've done better to use the stretch-wid attribute for a single turtle for this, though then this would've been trickier for collision detection, but I could've figured something out.
