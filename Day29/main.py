from tkinter import *
from tkinter import messagebox
import random
import pandas
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_input.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for char in range(int(spinbox_letter.get()))] 
    password_symbols = [random.choice(symbols)  for char in range(int(spinbox_symbol.get()))]
    password_numbers = [random.choice(numbers)  for char in range(int(spinbox_number.get()))]
    password_lists = password_letters + password_numbers + password_symbols
    random.shuffle(password_lists)
    password = "".join(password_lists)
    password_input.insert(0, password)
    pyperclip.copy(password)
    messagebox.showinfo(title="Copied", message="Generated password has been copied to clipboard!")

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_info():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    final_string = f"{website} | {email} | {password}\n"
    if website == "" or email == "" or password == "":
        messagebox.showinfo(title="Error", message="Please do not leave any of fields empty")

    
    else:
        yes_or_no = messagebox.askyesno(message=f"Entered details:\nEmail: {email}\nPassword: {password}\nAre you sure?",
                            title=f"{website}")
        
        if yes_or_no:
            with open(f"data", "a") as data:
                data.write(final_string)
                website_input.delete(0, END)
                email_input.delete(0, END)
                password_input.delete(0, END)
    
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=50, bg="white")

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

#Labels

website_label = Label(text="Website:", bg="white")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:", bg="white")
email_label.grid(row=2, column=0)

password_label = Label(text="Password:", bg="white")
password_label.grid(row=3, column=0)

password_letter = Label(text="Amount of Letters:", bg="white")
password_letter.grid(row=5, column=0)

password_number = Label(text="Amount of Numbers:", bg="white")
password_number.grid(row=6, column=0)

password_symbol = Label(text="Amount of Symbol:", bg="white")
password_symbol.grid(row=7, column=0)

#Entries

website_input = Entry(width=40)
website_input.grid(row=1, column=1, columnspan=2, sticky="EW")
website_input.focus()

email_input = Entry(width=40)
email_input.grid(row=2, column=1, columnspan=2, sticky="EW")
email_input.insert(0, "ornek@example.com")

password_input = Entry(width=21)
password_input.grid(row=3, column=1, sticky="EW")

#Buttons

pw_generator = Button(text="Generate Password", command=generate_password)
pw_generator.grid(row=3, column=2, sticky="EW")

pw_add = Button(text="Add", width=38, command=save_info, )
pw_add.grid(row=4, column=1, columnspan=2, sticky="EW")

#Password Content Spinboxes

spinbox_letter = Spinbox(from_=0, to=32, width=5)
spinbox_letter.grid(row=5, column=1)
spinbox_letter.delete(0, END)
spinbox_letter.insert(0, 8)

spinbox_number = Spinbox(from_=0, to=32, width=5)
spinbox_number.grid(row=6, column=1)
spinbox_number.delete(0, END)
spinbox_number.insert(0, 2)

spinbox_symbol = Spinbox(from_=0, to=32, width=5)
spinbox_symbol.grid(row=7, column=1)
spinbox_symbol.delete(0, END)
spinbox_symbol.insert(0, 2)


window.mainloop()