from tkinter import *
from tkinter import messagebox
import random
import string
import pyperclip
BACKGROUND = '#816f6f'
PATH = "C:/Users/bumos/Documents/data.txt"
PATH_LINUX = "/home/wtc/Documents/data.txt"
FONT_NAME = "Courier"




# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    alpha = list(filter(lambda x: x.isalpha(),[chr(i) for i in range(65, 122)]))
    numbers = "1234567890"
    punctuation = string.punctuation

    every_char = []

    for _ in range(10):
        every_char.append(random.choice(alpha))
        every_char.append(random.choice(numbers))
        every_char.append(random.choice(punctuation))


    chosen_pass = []

    for _ in range(8):
        chosen_pass.append(random.choice(every_char))

    random.shuffle(chosen_pass)
    password = "".join(chosen_pass)
    pass_input.insert(0, password)
    pyperclip.copy(pass_input.get())


  


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_pass():
    # email_input.get()
    em, web, pas = (email_input.get(), website_input.get(), pass_input.get())
    check_all = [True if len(i)> 0 else False for i in (em,web,pas)]

    


    if not all(check_all):
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=web, message=f"These are the details entered: \nEmail: {em}\nPassword: {pas}\nIs it ok to save?")
        if is_ok:
            with open(file=PATH, mode="a") as data:
                data.write(f"{web} |    {em} |     {pas}\n")
                # tkin
            messagebox.showinfo(title="created !!!!!!!!!!!!", message="You created the passmanager")
            email_input.delete(0, END)
            website_input.delete(0, END)
            pass_input.delete(0, END)

    

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
website_input = Entry(width=20, font=(FONT_NAME, 11, "normal"))
website_input.grid(row=1, column= 1, columnspan=3, pady=3, sticky="ew")

# ----------------------------------------------------------------------------------------------


# ----------------- -------------Email -----------------------------------------------------------------------
# -------------------EMAIL ADDRESS -----------------------------
email = Label(text="Email/Username", bg=BACKGROUND, font=(FONT_NAME,11, "normal"))
email.grid(column=0, row=2 )

# -------------- Email Input ----------------
email_input = Entry(font=(FONT_NAME,11, "normal"), width=20)
email_input.grid(row=2, column=1, columnspan=3, pady=3, sticky="ew")




# ---------------------- Password ----------------------------------------------------------------
# ------------------pass--------------------
password = Label(text="Password", font=(FONT_NAME, 11,"normal"), bg=BACKGROUND)
password.grid(row=3, column=0)

# ----------------pass_input -----------------
pass_input = Entry(font=(FONT_NAME,11, "normal"), width=20)
pass_input.grid(row=3, column=1,columnspan=2,  pady=3)

# ----------------------Generate Pass ------------------
generate_pass = Button(text="Generate password", width=15, command=password_generator)
generate_pass.grid(row=3,column=3, padx=3)


# ------------------ ADD ------------------------
add = Button(text="add", font=(FONT_NAME, 13, "normal"), command=save_pass)
add.grid(column=1, row=4, pady=5, columnspan=3, sticky="ew",)



# ----------- message box --------------------
# message =

window.mainloop()