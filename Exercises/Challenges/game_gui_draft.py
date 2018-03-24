from tkinter import *
import random

class Game:

    RULES = """

            I'm going to think of a number between 1 and 100                    
            while you try and guess what it is! Remember,                       
            you cannot guess a number less than 1 or greater than 100!         
            I'll give you hints with each guess on how close you are to         
            guessing my number. When you finally guess it, i'll tell
            you how many guesses it took! Good luck!

            """

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.lbl_title = Label(frame, text="Welcome to Guess the Number!")
        self.lbl_title.pack()

        self.lbl_result = Label(frame, text=self.RULES)
        self.lbl_result.pack()

        self.text_guess = Entry(frame, width=3)
        self.text_guess.pack()

        self.btn_check = Button(frame, text="Check", fg="green", command=self.check)
        self.btn_check.pack(side="left")

        self.btn_reset = Button(frame, text="Reset", fg="red", command=frame.quit())
        self.btn_reset.pack(side="right")

    def check(self):
        user_guess = int(self.text_guess.get())
        print(user_guess)


root = Tk()
game = Game(root)
root.mainloop()










