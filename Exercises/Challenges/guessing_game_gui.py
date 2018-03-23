import tkinter
import random










# player_guess = txt_guess.get()


# show result
# lbl_result['text'] = msg


class Game:

    RULES = """

            I'm going to think of a number between 1 and 100                    
            while you try and guess what it is! Remember,                       
            you cannot guess a number less than 1 or greater than 100!         
            I'll give you hints with each guess on how close you are to         
            guessing my number. When you finally guess it, i'll tell
            you how many guesses it took! Good luck!

            """

    ROOT = tkinter.Tk()

    def __init__(self):
        self.guesses = [0]
        self.current_guess = None
        self.mystery_number = random.randint(1, 100)

    def draw_labels(self):
        # create title widget
        lbl_title = tkinter.Label(Game.ROOT, text="Welcome to Guess the Number!")
        lbl_title.pack()

        # create sub text
        lbl_result = tkinter.Label(Game.ROOT, text=game.RULES)
        lbl_result.pack()

    def draw_buttons(self):
        # create check button
        btn_check = tkinter.Button(Game.ROOT, text="Check", fg="green", command=self.get_text_guess())
        btn_check.pack(side="left")

        # create reset button
        btn_reset = tkinter.Button(Game.ROOT, text="Reset", fg="red", command=Game.ROOT.quit())
        btn_reset.pack(side="right")


    def valid_guess(self, number):
        if 1 <= number <= 100:
            return True
        return False

    def get_text_guess(self):
        user_guess = int()
        # create input field
        guess_box = tkinter.Entry(Game.ROOT, width=3)

    def play_game(self):
        self.draw_labels()
        self.draw_buttons()
        self.get_text_guess()

        # Start the main events loop
        Game.ROOT.mainloop()
        Game.ROOT.destroy()





game = Game()
game.play_game()



