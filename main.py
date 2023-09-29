# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random
import pyperclip
import json

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letters = [random.choice(letters) for i in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for i in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for i in range(random.randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)
    password = "".join(password_list)

    pass_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

from tkinter import messagebox

def save():

    website = web_entry.get()
    email = email_entry.get()
    password = pass_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
    }}

    if len(website) == 0  or len(password) == 0:
        messagebox.showinfo(title="Warning!", message="Please do not leave the fields empty")
    else:
            try:
                with open("data.json", "r") as datafile:
                    data = json.load(datafile)  # Reading old data

            except FileNotFoundError:
                with open("data.json", "w") as datafile:
                    json.dump(new_data, datafile, indent=4)

            else:
                data.update(new_data)  # Updating old data with new data
                with open("data.json", "w") as datafile:
                    json.dump(data, datafile, indent=4)  # Saving updated data

            finally:
                web_entry.delete(0, END)
                pass_entry.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():
    website = web_entry.get()
    try:
        with open("data.json") as datafile:
            data = json.load(datafile)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message=f"No Data File Found!")
    else:
            if website in data:
                email = data[website]["email"]
                password = data[website]["password"]
                messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
            else:
                messagebox.showinfo(title="Error", message=f"No details for {website} found!")


# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)

logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#Labels
web_label = Label(text='Website:')
web_label.grid(row=1, column=0)

email_label = Label(text='Email/Username:')
email_label.grid(row=2, column=0)

pass_label = Label(text='Password:')
pass_label.grid(row=3, column=0)

#Entries
web_entry = Entry(width=21)
web_entry.grid(row=1, column=1)
web_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "ahmad@gmail.com")

pass_entry = Entry(width=21)
pass_entry.grid(row=3, column=1)

#Buttons
search_button = Button(text="Search", width=10, command=find_password)
search_button.grid(row=1, column=2)
generate_password_button = Button(text="Generate Password", width=11, command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text='Add', width=33, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()