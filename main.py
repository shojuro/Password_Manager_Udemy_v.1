from tkinter import *
from tkinter import ttk


BLACK ="#000000"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=BLACK)

canvas = Canvas(width=200, height=200, bg=BLACK, highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1,row=0)
# canvas.grid(column=1, row=1)
# Labels
web_label = Label(text="Website:", bg=BLACK,anchor='e', fg="White", font=("Courier", 12))
web_label.grid(column=0,row=1)

email_username_label = Label(text="Email/Username:", bg=BLACK, fg="White", font=("Courier", 12))
email_username_label.grid(column=0,row=2)

pw_label = Label(text="Password:", bg=BLACK, fg="White", font=("Courier", 12))
pw_label .grid(column=0,row=3)

# Entries
# web_entry = Entry(bg="White", width=64)
# # web_entry.config()
# web_entry.grid(column=1, row=1, columnspan=2)
web_entry = Entry(bg="White", width=64)
web_entry.grid(column=1, row=1, columnspan=2)

email_username_entry = Entry(bg="White", justify="left", width=64)
email_username_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(bg="White", width=33)
password_entry.grid(column=1, row=3)

# Buttons
gen_password_button = Button(text="Generate Password",justify= "left", bg="White", font=("Courier", 12, "bold"))
gen_password_button.grid(column=2, row=3)

add_button = Button(text="Add", bg="White", width= 38, font=("Courier", 12, "bold"))
add_button.grid(column=1, row=4, columnspan=2)





window.mainloop()