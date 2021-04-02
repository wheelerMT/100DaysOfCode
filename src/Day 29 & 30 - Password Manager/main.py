import tkinter
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]
    random.shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password)
    password_entry.delete(0, tkinter.END)
    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_details():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }
    if len(website_entry.get()) == 0 or len(password_entry.get()) == 0:
        messagebox.showerror(title="Error", message="Error: please fill in all fields.")
        return

    else:
        try:
            with open("data.json", "r") as file:
                # Reading old data
                data = json.load(file)
                # Updating old data
                data.update(new_data)
            with open("data.json", "w") as file:
                # Saving updated data
                json.dump(data, file, indent=4)

        except FileNotFoundError:
            file = open("data.json", "w")
            json.dump(new_data, file, indent=4)

    # Clear website and password fields
    for entry in [website_entry, password_entry]:
        entry.delete(0, tkinter.END)
    website_entry.focus()


# ---------------------------- PASSWORD FINDER -------------------------- #
def find_password():
    """
    Searches the data.json to see if details for entered website already exist.
    """
    try:
        with open("data.json", "r") as file:
            saved_details = json.load(file)
            website_is_saved = False
            for website in saved_details:
                if website == website_entry.get():
                    website_is_saved = True
                    saved_email = (saved_details.get(website)).get("email")
                    saved_pw = (saved_details.get(website)).get("password")
                    # Print details to screen
                    messagebox.showinfo(message=f"Website: {website}\n"
                                                f"Email: {saved_email}\n"
                                                f"Password: {saved_pw}")
            if not website_is_saved:
                messagebox.showinfo(message="No details for the website exists.")
    except FileNotFoundError:
        messagebox.showerror(message="No Data File Found.")


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = tkinter.Canvas(width=200, height=200, highlightthickness=0)
logo_image = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

# Labels
website_label = tkinter.Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = tkinter.Label(text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = tkinter.Label(text="Password:")
password_label.grid(row=3, column=0)

# Entry fields
website_entry = tkinter.Entry(width=34)
website_entry.grid(row=1, column=1, sticky="EW")
website_entry.focus()

email_entry = tkinter.Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2, sticky="EW")
email_entry.insert(0, "matt@email.com")

password_entry = tkinter.Entry(width=34)
password_entry.grid(row=3, column=1)

# Buttons
gen_password_btn = tkinter.Button(text="Generate Password", command=generate_password)
gen_password_btn.grid(row=3, column=2, sticky="EW")

add_details_btn = tkinter.Button(text="Add", width=36, command=add_details)
add_details_btn.grid(row=4, column=1, columnspan=2, sticky="EW")

search_button = tkinter.Button(text="Search", command=find_password)
search_button.grid(row=1, column=2, sticky="EW")

window.mainloop()
