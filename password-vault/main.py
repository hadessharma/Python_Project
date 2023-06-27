from tkinter import *
import random

DEFAULT_USER = 'scsa'
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    with open('./password-vault/pass.txt', 'a') as file:
        file.write(f'{entry_website.get()} | {entry_user.get()} | {entry_pass.get()}\n')
    
    # clear fields once saved
    entry_pass.delete(0, END)
    entry_website.delete(0, END)
    
    #focus back to website entry
    entry_website.focus()
    
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx= 20, pady= 20)

canvas = Canvas(width=200, height=200)
lock_image = PhotoImage(file='./password-vault/logo.png')
canvas.create_image(100, 100, image = lock_image)
canvas.grid(column=1, row=0)

# website entry
label_website = Label(text='Website:')
label_website.grid(column=0, row=1)

entry_website = Entry(width=35)
entry_website.grid(column=1, row= 1, columnspan=2, sticky='EW')
entry_website.focus()
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

button_generate_pass = Button(text='Generate Password', width=15)
button_generate_pass.grid(column=2, row=3, sticky='EW')

# add button

button_add = Button(text='Add', width=36, command=save_password)
button_add.grid(column=1, row=4, columnspan=2, sticky='EW')

    
window.mainloop()