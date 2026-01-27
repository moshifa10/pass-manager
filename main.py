from tkinter import *
BACKGROUND = '#816f6f'
PATH = '/C:/Users/bumos/Documents'
FONT_NAME = "Courier"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.minsize(height=400, width=500)
window.title("Password Manager")
window.config(bg=BACKGROUND, padx=50, pady=50)

# canvas
canvas = Canvas(width=200, height=224, bg=BACKGROUND, highlightthickness=0)
photo = PhotoImage(file="./logo.png")
canvas.create_image(100, 112, image=photo)
canvas.grid(column=1, row=0)

# ----------------------------------------------------------------------------------
# ---------------- label Website ----------------
website = Label(text="Website:", font=(FONT_NAME,11, "normal"), bg=BACKGROUND)
website.grid(row=1, column=0)

# ------------- Website input --------------
website_input = Entry(width=20, font=(FONT_NAME, 11, "normal"))
website_input.grid(row=1, column= 1)
# ----------------------------------------------------------------------------------




window.mainloop()