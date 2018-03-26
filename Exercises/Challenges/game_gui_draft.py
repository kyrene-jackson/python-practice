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

        self.mystery_number = random.randint(1, 100)
        self.guesses = [0]
        self.current_guess = None

        # self.lbl_title = Label(frame, text="Welcome to Guess the Number!")
        # self.lbl_title.pack()

        self.message = "Guess a number from 1 to 100"
        self.label_text = StringVar()
        self.label_text.set(self.message)
        self.label = Label(master, textvariable=self.label_text)

        vcmd = master.register(self.validate)
        self.entry = Entry(master, validate="key", validatecommand=(vcmd, '%P'))

        # self.lbl_result = Label(frame, text=self.RULES)
        # self.lbl_result.pack()

        self.text_guess = Entry(frame, width=3)
        self.text_guess.pack()

        self.btn_guess = Button(frame, text="Guess", fg="green", command=self.guess_number)
        self.btn_guess.pack(side="left")

        self.btn_reset = Button(frame, text="Play Again", fg="red", command=self.reset, state=DISABLED)
        self.btn_reset.pack(side="right")


    def validate(self, new_text):
        if not new_text:
            self.guess = None
            return True

        try:
            guess = int(new_text)
            if 1 <= guess <= 100:
                self.current_guess = guess

                print(self.mystery_number)
                print(self.guesses)
                print(self.current_guess)

                return True
            else:
                return False
        except ValueError:
            return False

    def guess_number(self):

        self.guesses.append(self.current_guess)

        if self.current_guess is None:
            self.message = "Guess a number from 1 to 100"
        elif self.current_guess == self.mystery_number:
            self.message = "Congratulations! You guessed the number! It took you {} try(s)".format(len(self.guesses))
            self.btn_guess.configure(state="DISABLED")
            self.btn_reset.configure(state="NORMAL")

        elif self.current_guess < self.mystery_number:
            self.message = "Too low!"
        else:
            self.message = "Too high!"

    def reset(self):
        self.entry.delete(0, END)
        self.mystery_number = random.randint(1, 100)
        self.current_guess = 0
        self.guesses = [0]

        self.message = "Guess a number from 1 to 100"
        self.label_text.set(self.message)

        self.btn_guess.configure(state=NORMAL)
        self.btn_reset.configure(state=DISABLED)

    # def get_player_guess(self):
    #     while True:
    #         try:
    #             player_guess = int(self.text_guess.get())
    #         except ValueError:
    #             self.lbl_result["text"] = "Oops! That was not a valid number, try again..."
    #             continue
    #
    #         if self.valid_guess(player_guess):
    #
    #             self.current_guess = player_guess
    #
    #             if self.first_round():
    #                 self.play_first_round()
    #             else:
    #                 self.play_round()
    #
    #             self.add_to_guess_list(player_guess)
    #             self.lbl_result["text"] = self.RULES
    #
    #             print(self.mystery_number)
    #             print(self.current_guess)
    #             print(self.guesses)
    #
    #             return self.current_guess
    #         else:
    #             self.lbl_result["text"] = "OUT OF BOUNDS!"
    #
    # def valid_guess(self, number):
    #     if 1 <= number <= 100:
    #         return True
    #     return False
    #
    # def first_round(self):
    #     return len(self.guesses) == 1
    #
    # def total_guess_count(self):
    #     return len(self.guesses)
    #
    # def correct_number(self):
    #     return self.current_guess == self.mystery_number
    #
    # def previous_guess(self, guess_list):
    #     return guess_list[-1]
    #
    # def add_to_guess_list(self, number):
    #     return self.guesses.append(number)
    #
    # def is_in_range(self, player_number):
    #     return abs(self.mystery_number - player_number) in range(1, 11)
    #
    # def play_first_round(self):
    #     if self.is_in_range(self.current_guess):
    #         self.lbl_result["text"] = "WARM!"
    #     else:
    #         self.lbl_result["text"] = "COLD!"
    #
    # def play_round(self):
    #     if self.guess_is_closer(self.guesses):
    #         self.lbl_result["text"] = "WARMER!"
    #     else:
    #         self.lbl_result["text"] = "COLDER!"
    #
    # def guess_is_closer(self, guess_list):
    #     if abs(self.mystery_number - self.current_guess) < abs(self.mystery_number - self.previous_guess(guess_list)):
    #         return True
    #     return False


root = Tk()
game = Game(root)

root.mainloop()
root.destroy()










