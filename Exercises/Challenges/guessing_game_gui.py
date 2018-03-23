import tkinter







# Create root window
root = tkinter.Tk()


# Create widgets
lbl_title = tkinter.Label(root, text="Welcome to the Guessing Game!")
lbl_title.pack()

lbl_result = tkinter.Label(root, text="Good Luck!")
lbl_result.pack()

btn_check = tkinter.Button(root, text="Check", fg="green", command=root.quit())
btn_check.pack(side="left")

btn_reset = tkinter.Button(root, text="Reset", fg="red", command=root.quit())
btn_reset.pack(side="right")

txt_guess = tkinter.Entry(root, width=3)
txt_guess.pack()

# Start the main events loop
root.mainloop()
root.destroy()
