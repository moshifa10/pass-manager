from tkinter import *
BACKGROUND = '#816f6f'
PATH = '/C:/Users/bumos/Documents'

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(bg=BACKGROUND,padx=70, pady=70)

canvas = Canvas(width=200, height=224, bg=BACKGROUND, highlightthickness=0)
photo = PhotoImage(file="./logo.png")
canvas.create_image(100, 112, image=photo)
canvas.grid(column=1, row=0)

window.mainloop()