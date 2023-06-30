from tkinter import *
from tkinter import messagebox
import pyperclip
import random
import string
import json

DEFAULT_USER = 'abcd@gmail.com'

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    
    
    s_lower  = list(string.ascii_lowercase)
    s_upper  = list(string.ascii_uppercase)
    s_digits = list(string.digits)
    s_pun    = list(string.punctuation)

    random.shuffle(s_lower)
    random.shuffle(s_upper)
    random.shuffle(s_digits)
    random.shuffle(s_pun)

    len_of_password = random.randint(8,12)

    part1 = round(len_of_password * .3)
    part2 = round(len_of_password * .2)

    password = []

    for _ in range(part1):
        password.append(s_lower[_])
        password.append(s_upper[_])
    
    for _ in range(part2):
        password.append(s_digits[_])
        password.append(s_pun[_])

    random.shuffle(password)
    password = ''.join(password)
    
    entry_pass.delete(0, END)
    entry_pass.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    
    
    # check if website or password is empty
    if len(entry_website.get()) == 0:
        messagebox.showerror(title='Website!', message='Please enter valid website.')
        return
    if len(entry_pass.get()) == 0:
        messagebox.showerror(title='Password!', message='Please enter a valid password')
        return
    
    new_data = {
        entry_website.get() : {
            'password': entry_pass.get(),
            'user'    : entry_user.get(),
        }
    }
    
    # checking if the details submitted is okay
    is_okay = messagebox.askokcancel(title=entry_website.get(), message=f'These are the details entered: \nEmail: {entry_user.get()}\nPassword: {entry_pass.get()}')

    if is_okay:   
        # save password into the file pass.json
        try:
            with open('./password-manager/pass.json', 'r') as data_file:
                data = json.load(data_file)
                data.update(new_data)
        except: # when json file is empty
            with open('./password-manager/pass.json', 'w') as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            with open('./password-manager/pass.json', 'w') as data_file:
                json.dump(data, data_file, indent=4)
        finally:    
            # clear fields once saved
            entry_pass.delete(0, END)
            entry_website.delete(0, END)
            
            # focus back to website entry
            entry_website.focus()
    
# ---------------------------- SEARCH PASSWORD ------------------------------- #

def search_password():
    
    
    with open('./password-manager/pass.json', 'r') as data_file:
        data = json.load(data_file)
        try:
            messagebox.showinfo(title='Password found', message= f'For {entry_website.get()},\n user: {data.get(entry_website.get()).get("user")}\n pass: {data.get(entry_website.get()).get("password")}')
        except:
            messagebox.showerror(title='Passowrd not found', message= f'No data found for {entry_website.get()}')
            
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx= 20, pady= 20)

canvas = Canvas(width=200, height=200)
lock_image = PhotoImage(file='./password-manager/logo.png')
canvas.create_image(100, 100, image = lock_image)
canvas.grid(column=1, row=0)

# website entry
label_website = Label(text='Website:')
label_website.grid(column=0, row=1)

entry_website = Entry(width=21)
entry_website.grid(column=1, row= 1, columnspan=1, sticky='EW')
entry_website.focus()

# search button
button_search = Button(text='Search', command=search_password)
button_search.grid(column=2, row=1, sticky='EW')

# email/username entry
label_user = Label(text='Email/Username:')
label_user.grid(column=0, row=2)

entry_user = Entry(width=35)
entry_user.grid(column=1, row=2, columnspan=2, sticky='EW')
entry_user.insert(0, DEFAULT_USER)

# Password entry
label_pass = Label(text='Password:')
label_pass.grid(column=0, row=3)

entry_pass = Entry(width=21)
entry_pass.grid(column=1, row=3, sticky='EW')

# generate password button
button_generate_pass = Button(text='Generate Password', width=15, command=generate_password)
button_generate_pass.grid(column=2, row=3, sticky='EW')

# add button
button_add = Button(text='Add', width=36, command=save_password)
button_add.grid(column=1, row=4, columnspan=2, sticky='EW')

    
window.mainloop()