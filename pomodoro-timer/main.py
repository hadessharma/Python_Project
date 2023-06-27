from tkinter import *
import time
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global REPS
    REPS = 0
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text = f'00:00')
    label_tick.config(text='')
    label_top.config(text='TIMER!', fg=GREEN)
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global REPS
    REPS += 1
    if REPS % 8 == 0:
        count_down(LONG_BREAK_MIN*60)
        label_top.config(text='LONG BREAK!', fg=RED)
        label_tick.config(text= label_tick.cget('text') + (u'\N{check mark}'))
    elif REPS%2 == 0:
        count_down(SHORT_BREAK_MIN*60)
        label_top.config(text='SHORT BREAK!', fg=PINK)
    else:
        count_down(WORK_MIN*60)
        label_top.config(text='WORK NOW!', fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f'0{count_sec}'
        
    canvas.itemconfig(timer_text, text= f'{count_min}:{count_sec}')
    if count > 0:
       timer =  window.after(1000, count_down, count - 1)
    else:
        start_timer()
        
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

label_tick = Label(font=(FONT_NAME, 15, 'bold'), bg=YELLOW, fg=GREEN)
label_tick.grid(column=1, row=3)


window.mainloop()
