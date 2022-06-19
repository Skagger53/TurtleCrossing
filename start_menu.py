if __name__ == "__main__": print("This is a supporting file. Do not execute directly.")
else:
    import tkinter as tk
    from PIL import ImageTk, Image

    opening = """
    Therese is a beautiful, curious turtle who loves making new friends! She just moved to a new city to start her dream job of managing a nursing facility for disabled and needy animals. In her new location, she's become fast friends with all kinds of new animals, include many chickens.

    Therese keeps hearing others ask "why did the chicken cross the road?" ... and she has no idea! Strangely, all her chicken friends get in a huff when she tries to ask them, and she doesn't want to offend by continuing to bring it up. The question is keeping her up at night...why, WHY, do chickens cross the road?

    Being the inquisitive turtle she is, Therese has decided she's going to find out what all the fuss is about and cross the road a few times herself! Walk in the shoes of a chicken for a bit!

    Will you help Therese cross the road and discover what the big deal is with chickens and roads? Will you help Therese sleep better at night, so she can focus on helping those in need at her job?

    (During the game, press spacebar to pause. Press "q" to quit.)

    """

    def starting_screen(difficulty): # The opening screen. This is the first thing the user sees. It introduces the game and allows the user to set the difficulty.
        def assign_difficulty(option): # Called when any option is chosen (including Quit)
            nonlocal difficulty
            difficulty = option
            starting_screen.destroy()

        starting_screen = tk.Tk()
        starting_screen.geometry("1050x640")
        starting_screen.title("Of Turtles and Chickens")

        # Placing Therese's beautiful glamour shot!
        therese_glamour_shot = ImageTk.PhotoImage(Image.open("curious_therese.png"))
        therese_glamour_shot_label = tk.Label(starting_screen, image = therese_glamour_shot)
        therese_glamour_shot_label.grid(row = 0, rowspan = 5, column = 5)

        # Setting the title of the game's intro text
        game_title = tk.Label(starting_screen, text = "\nOf Turtles and Chickens", font = "Arial 12 bold")
        game_title.grid(row = 0, columnspan = 5)

        # Setting the game's intro text
        game_description = tk.Label(starting_screen, text = opening, width = 70, wraplength = 500, justify = "left")
        game_description.grid(row = 1, columnspan = 5)

        # Setting all buttons for game mode and to quit
        option0 = tk.Button(starting_screen, text = "Easy", command = lambda: assign_difficulty(0))
        option0.grid(row = 2, column = 0)
        option1 = tk.Button(starting_screen, text = "Normal", command = lambda: assign_difficulty(1))
        option1.grid(row = 2, column = 1)
        option3 = tk.Button(starting_screen, text = "Hard", command = lambda: assign_difficulty(3))
        option3.grid(row = 2, column = 2)
        option4 = tk.Button(starting_screen, text = "Insane", command = lambda: assign_difficulty(4))
        option4.grid(row = 2, column = 3)
        label = tk.Label()
        label.grid(row = 3, column = 0)
        quit = tk.Button(starting_screen, text = "Quit", command = lambda: assign_difficulty(5))
        quit.grid(row = 4, column = 1, columnspan = 2)

        starting_screen.mainloop()

        return difficulty