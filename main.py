from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def gen():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]
    shuffle(password_list)
    password = "".join(password_list)

    pass_entry.insert(0, string=password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = web_entry.get()
    username = user_entry.get()
    password = pass_entry.get()
    new_data = {
        website: {
            "email": username,
            "password": password
        }
    }
    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showinfo(message="Entries left empty, try again")
    else:
        try:
            with open("password_list.json", mode="r") as new_file:
                data = json.load(new_file)
                data.update(new_data)
            with open("password_list.json", mode="w") as new_file:
                json.dump(data, new_file, indent=4)
        except FileNotFoundError:
            with open("password_list.json", mode="w") as new_file:
                json.dump(new_data, new_file, indent=4)
        web_entry.delete(0, END)
        pass_entry.delete(0, END)


# ---------------------------- Search --------------------------------- #
def find_pass():
    site = web_entry.get()
    try:
        with open("password_list.json", mode="r") as data_file:
            data = json.load(data_file)
            messagebox.showinfo(message=f"Username: {data[site]['email']}\nPassword: "
                                        f"{data[site]['password']}")
    except FileNotFoundError:
        messagebox.showinfo(message="No Data File Found")
    except KeyError:
        messagebox.showinfo(message="No details for the website exist")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Generator")
window.config(pady=50, padx=50)

canvas = Canvas(height=200, width=200)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)

pass_label = Label(text="Password:")
pass_label.grid(column=0, row=3)

# Buttons
gen_pass = Button(text="Generate Password", width=10, command=gen)
gen_pass.grid(column=2, row=3)

add = Button(text="Add", width=33, command=save)
add.grid(column=1, row=4, columnspan=2)

search = Button(text="Search", width=10, command=find_pass)
search.grid(column=2, row=1)

# Entries
web_entry = Entry(width=21)
web_entry.grid(column=1, row=1)
web_entry.focus()
user_entry = Entry(width=35)
user_entry.grid(column=1, row=2, columnspan=2)
user_entry.insert(0, string="Your Email Here")
pass_entry = Entry(width=21)
pass_entry.grid(column=1, row=3)

window.mainloop()
