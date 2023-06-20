from tkinter import *

def calculate():
    entry_kms.select_clear()
    entry_kms.insert(0, '%0.2f' % (int(entry_miles.get()) * 1.609344)) 
    
window = Tk()
window.title('Miles to KM')
window.minsize(height=100, width=200)
window.config(padx=10, pady=10)

label_is_equal = Label(text='is equal to')
label_is_equal.grid(column=0, row=1)

entry_miles = Entry(width=10)
entry_miles.grid(column=1, row=0)

label_miles = Label(text='Miles')
label_miles.grid(column=2, row=0)

entry_kms = Entry(width=10)
entry_kms.grid(column=1, row=1)

label_kms = Label(text='Kms')
label_kms.grid(column=2, row=1)

button_calc = Button(text='Calculate', command=calculate)
button_calc.grid(column=1, row=2)


window.mainloop()