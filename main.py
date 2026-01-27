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
canvas = Canvas(width=250, height=224, bg=BACKGROUND, highlightthickness=0, )
photo = PhotoImage(file="./logo.png")
canvas.create_image(250//2, 112, image=photo)
canvas.grid(column=1, row=0)

# --------------------------------------------------------------------------------------------
# ---------------- label Website ----------------
website = Label(text="Website:", font=(FONT_NAME,11, "normal"), bg=BACKGROUND)
website.grid(row=1, column=0)

# ------------- Website input --------------
website_input = Entry(width=15, font=(FONT_NAME, 11, "normal"))
website_input.grid(row=1, column= 1, columnspan=3, pady=2)

# ----------------------------------------------------------------------------------------------


# ----------------- -------------Email -----------------------------------------------------------------------
# -------------------EMAIL ADDRESS -----------------------------
email = Label(text="Email/Username", bg=BACKGROUND, font=(FONT_NAME,11, "normal"))
email.grid(column=0, row=2 )

# -------------- Email Input ----------------
email_input = Entry(font=(FONT_NAME,11, "normal"), width=15)
email_input.grid(row=2, column=1, columnspan=3, pady=2)



# ---------------------- Password ----------------------------------------------------------------
# ------------------pass--------------------
password = Label(text="Password", font=(FONT_NAME, 11,"normal"), bg=BACKGROUND)
password.grid(row=3, column=0)

# ----------------pass_input -----------------
pass_input = Entry(font=(FONT_NAME,11, "normal"), width=15)
pass_input.grid(row=3, column=1, columnspan=3, pady=2)

# ----------------------Generate Pass ------------------
generate_pass = Button(text="Generate password", width=15)
generate_pass.grid(row=3,column=3, padx=20, pady=20)
window.mainloop()