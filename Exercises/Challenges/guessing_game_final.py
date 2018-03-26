import random
from tkinter import *

class GuessingGame:

    RULES = """

            I'm going to think of a number between 1 and 100                    
            while you try and guess what it is! Remember,                       
            you cannot guess a number less than 1 or greater than 100!         
            I'll give you hints with each guess on how close you are to         
            guessing my number. When you finally guess it, i'll tell
            you how many guesses it took! Good luck!

            """

    def __init__(self, master):
        self.master = master
        master.title("Guessing Game")

        self.secret_number = random.randint(1, 100)
        self.guess = None
        self.num_guesses = [0]

        self.message = self.RULES
        self.label_text = StringVar()
        self.label_text.set(self.message)
        self.label = Label(master, textvariable=self.label_text)

        vcmd = master.register(self.validate)
        self.entry = Entry(master, validate="key", validatecommand=(vcmd, '%P'))

        self.guess_button = Button(master, text="Guess", command=self.guess_number)
        self.reset_button = Button(master, text="Play again", command=self.reset, state=DISABLED)

        self.label.grid(row=0, column=0, columnspan=2, sticky=W+E)
        self.entry.grid(row=1, column=0, columnspan=2, sticky=W+E)
        self.guess_button.grid(row=2, column=0)
        self.reset_button.grid(row=2, column=1)

    def validate(self, new_text):
        if not new_text:
            self.guess = None
            return True

        try:
            guess = int(new_text)
            if 1 <= guess <= 100:
                self.guess = guess
                return True
            else:
                return False
        except ValueError:
            self.message = "Oops! That was not a valid number, try again..."
            return False

    def guess_number(self):
        self.num_guesses.append(self.guess)

        if self.guess is None:
            self.message = self.RULES

        elif self.guess == self.secret_number:
            self.message = "Congratulations! You guessed the number after {} try(s)".format(len(self.num_guesses))
            self.guess_button.configure(state=DISABLED)
            self.reset_button.configure(state=NORMAL)

        if self.first_round():
            if self.in_range():
                self.message = "WARM!"
            else:
                self.message = "COLD!"
        elif not self.first_round():
            if self.closer():
                self.message = "WARMER!"
            else:
                self.message = "COLDER!"

        # elif self.guess < self.secret_number:
        #     self.message = "Too low! Guess again!"
        # else:
        #     self.message = "Too high! Guess again!"

        self.label_text.set(self.message)

    def reset(self):
        self.entry.delete(0, END)
        self.secret_number = random.randint(1, 100)
        self.guess = 0
        self.num_guesses = 0

        self.message = self.RULES
        self.label_text.set(self.message)

        self.guess_button.configure(state=NORMAL)
        self.reset_button.configure(state=DISABLED)

    def first_round(self):
        return len(self.num_guesses) == 2

    def in_range(self):
        return abs(self.secret_number - self.guess) in range(1, 11)

    def previous_guess(self):
        return self.num_guesses[-1]

    def closer(self):
        if abs(self.secret_number - self.guess) < abs(self.secret_number - self.previous_guess()):
            return True
        return False





root = Tk()
my_gui = GuessingGame(root)
root.mainloop()