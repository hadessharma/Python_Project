from tkinter import *
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"

try:
    df       = pd.read_csv('./flashcard-app/data/words_to_learn.csv')
    data_raw     = df.to_dict(orient='records')
except:
    df   = pd.read_csv('./flashcard-app/data/french_words.csv')
    data_raw = df.to_dict(orient='records')
    
data_list = [ {i['French'] : i['English']} for i in data_raw]

# selecting first random word
random_data = random.choice(data_list)

new_df = {}
# ------------------------------------ known function ------------------------------------ #
def know_button():
    global random_data, flip_timer, data_raw
    window.after_cancel(flip_timer)
    
    # checking if button clicked before the card flipped or after
    if canvas.itemcget(card_title, 'text') == 'English':
        data_list.remove({ list(random_data.keys())[0] : canvas.itemcget(card_word, 'text')})
    else:
        data_list.remove({ canvas.itemcget(card_word, 'text') : list(random_data.values())[0]})
        
    random_data = random.choice(data_list)
    
    # chaning the UI config back
    canvas.itemconfig(card_word, text = list(random_data.keys())[0], fill = 'black')
    canvas.itemconfig(card_title, text = 'French', fill = 'black')
    canvas.itemconfig(card_image, image= image_card_front)
    
    flip_timer = window.after(3000, flip_card)
    
    # updating words_to_learn csv file by removing the word that is known
    new_df = pd.DataFrame([{'French': list(item.keys())[0], "English": list(item.values())[0]} for item in data_list])
    new_df.to_csv('./flashcard-app/data/words_to_learn.csv', index=False)
# ------------------------------------ unkown function ------------------------------------ #

def unkown_button():
    global random_data, flip_timer
    window.after_cancel(flip_timer)
    
    # picking new word if guessed wrong
    random_data = random.choice(data_list)
    
    # changing the UI config back
    canvas.itemconfig(card_word, text = list(random_data.keys())[0], fill = 'black')
    canvas.itemconfig(card_image, image= image_card_front)
    canvas.itemconfig(card_title, text = 'French', fill = 'black')
    
    flip_timer = window.after(3000, flip_card)
    
# ------------------------------------       UI        ------------------------------------ #

def flip_card():
    global random_data
    canvas.itemconfig(card_image, image = image_card_back)
    canvas.itemconfig(card_title, text = 'English', fill = 'white')
    canvas.itemconfig(card_word, text = list(random_data.values())[0], fill = 'white')
    
window = Tk()
window.title('Flashcard App')   
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)


flip_timer = window.after(ms=3000, func=flip_card)


canvas = Canvas(width=800, height=526)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

image_card_front = PhotoImage(file='./flashcard-app/images/card_front.png')
image_card_back = PhotoImage(file='./flashcard-app/images/card_back.png')

card_image        = canvas.create_image(400, 263 , image = image_card_front)

card_title = canvas.create_text(400, 150, text='French', font=('Ariel', 40, "italic"))
card_word  = canvas.create_text(400, 263, text=list(random_data.keys())[0], font=('Ariel', 60, 'bold'))

canvas.grid(column=0, row=0, columnspan=2)


image_right = PhotoImage(file='./flashcard-app/images/right.png')
button_know = Button(image=image_right, highlightthickness=0, command=know_button)
button_know.grid(column= 1, row= 1)

image_wrong = PhotoImage(file='./flashcard-app/images/wrong.png')
button_unkown = Button(image=image_wrong, highlightthickness=0, command=unkown_button)
button_unkown.grid(column= 0, row= 1)



image_card_back = PhotoImage(file='./flashcard-app/images/card_back.png')

# canvas.create_image(400, 263, image = image_card_back)


window.mainloop()