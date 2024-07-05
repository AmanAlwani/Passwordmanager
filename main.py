from tkinter import *
from tkinter import messagebox
import tkinter
import random
import pyperclip
import json
import os
import sys


def resource_path(relative_path):
    try:
        base_path = sys.MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


# --------------Save Password--------------
def takevalues():
    web = w_name.get()
    user = email.get()
    p_word = password.get()
    new_data = {
        web: {
            'E-mail': user,
            'Password': p_word
        }
    }
    if web == '' or p_word == '' or user == '':
        messagebox.showinfo(title='Oops', message='Please don\'t leave and fields empty!!')
    else:
        try:
            with open(resource_path('password.json'), 'r') as datafiles:
                data = json.load(datafiles)
                data.update(new_data)
            with open(resource_path('password.json'), 'w') as datafiles:
                json.dump(data, datafiles, indent=4)
        except:
            with open(resource_path('password.json'), 'w') as datafiles:
                json.dump(new_data, datafiles, indent=4)
        website_entry.delete(0, END)
        password_entry.delete(0, END)


# ------------------Password Generator------------------

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_pass():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for char in range(nr_letters)]
    password_numbers = [random.choice(symbols) for char in range(nr_symbols)]
    password_symbols = [random.choice(numbers) for char in range(nr_numbers)]
    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    r_password = ''.join(password_list)
    password_entry.insert(0, r_password)
    pyperclip.copy(r_password)


# --------------------Searching---------------------
def searching():
    s_website = w_name.get()
    try:
        with open(resource_path('password.json'), 'r') as datafiles:
            data = json.load(datafiles)
    except FileNotFoundError:
        messagebox.showinfo(title='Error', message='Database is empty!!')
    else:
        if s_website in data:
            s_email = data[s_website]['E-mail']
            s_password = data[s_website]['Password']
            messagebox.showinfo(title=f'{s_website}', message=f'E-mail/Username - {s_email}\nPassword - {s_password}')
            pyperclip.copy(s_password)
        else:
            messagebox.showinfo(title='Error', message=f'Website-{s_website} was not found in the database.')


# --------------UI SETUP--------------
window = Tk()
window.title('Password Manager🔑')
window.config(padx=20, pady=20)
canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file=resource_path('logo.png'))
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

w_name = tkinter.StringVar()
email = tkinter.StringVar()
password = tkinter.StringVar()

Website_label = Label(text='Website :')
Website_label.grid(row=1, column=0, sticky='e')
website_entry = Entry(window, width=26, textvariable=w_name)
website_entry.grid(row=1, column=1, columnspan=2, sticky='EW')
website_entry.focus()

search_button = Button(text='Search', command=searching, width=14)
search_button.grid(row=1, column=2, sticky='EW')

email_label = Label(text='E-mail/Username :')
email_label.grid(row=2, column=0, sticky='e')
email_entry = Entry(window, width=40, textvariable=email)
email_entry.grid(row=2, column=1, columnspan=2, sticky='EW')
email_entry.insert(END, 'aman2102004@gmail.com')

password_label = Label(text='Password :')
password_label.grid(row=3, column=0, sticky='e')
password_entry = Entry(window, width=26, textvariable=password)
password_entry.grid(row=3, column=1, columnspan=1, sticky='EW')

generate_button = Button(text='Generate Password', width=14, command=generate_pass)
generate_button.grid(row=3, column=2, sticky='EW')
add_button = Button(text='Add', width=36, command=takevalues)
add_button.grid(row=4, column=1, columnspan=2, sticky='EW')
window.mainloop()
