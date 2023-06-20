from tkinter import *
import time
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 
def start_timer():
    count_down(25.00)

def reset_timer():
    pass
# ---------------------------- TIMER MECHANISM ------------------------------- # 
       
    
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    if count<0:
        return
    canvas.itemconfig(timer_text, text = '%.2f' % count)
    window.after(1000, count_down, count-.01)
        
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pamodoro')
window.config(padx=100, pady=50, bg=YELLOW)


# canvas
canvas     = Canvas(width=200, height=224, bg=YELLOW, highlightbackground=YELLOW)
tamato_img = PhotoImage(file='./pomodoro-timer/tomato.png')
canvas.create_image(102, 112, image=tamato_img)
timer_text = canvas.create_text(102, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))

canvas.grid(column=1, row=1)

# top label

label_top = Label(text='Timer', font=(FONT_NAME, 40, 'bold'), bg=YELLOW, fg=GREEN)
label_top.grid(column=1, row=0)

# start button

button_start = Button(text='Start', command=start_timer)
button_start.grid(column=0, row=2)

# reset button

button_reset = Button(text='Reset', command=reset_timer)
button_reset.grid(column=2, row=2)

# tick marks at the bottom

label_tick = Label(text=u'\N{check mark}', font=(FONT_NAME, 15, 'bold'), bg=YELLOW, fg=GREEN)
label_tick.grid(column=1, row=3)


window.mainloop()
