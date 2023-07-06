from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

# ------------------------------------ known function ------------------------------------ #
def know_button()
# ------------------------------------ unkown function ------------------------------------ #

# ------------------------------------       UI        ------------------------------------ #

window = Tk()
window.title('Flashcard App')   
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

canvas = Canvas(width=800, height=526)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

image_card_front = PhotoImage(file='./flashcard-app/images/card_front.png')
canvas.create_image(400, 263 , image = image_card_front)

canvas.create_text(400, 150, text='Title', font=('Ariel', 40, "italic"))
canvas.create_text(400, 263, text='Word', font=('Ariel', 60, 'bold'))

canvas.grid(column=0, row=0, columnspan=2)


image_right = PhotoImage(file='./flashcard-app/images/right.png')
button_know = Button(image=image_right, highlightthickness=0)
button_know.grid(column= 1, row= 1)

image_wrong = PhotoImage(file='./flashcard-app/images/wrong.png')
button_unkown = Button(image=image_wrong, highlightthickness=0)
button_unkown.grid(column= 0, row= 1)



image_card_back = PhotoImage(file='./flashcard-app/images/card_back.png')


# canvas.create_image(400, 263, image = image_card_back)


window.mainloop()