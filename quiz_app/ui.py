from tkinter import *

THEME_COLOR = "#375362"

class QuizInterface:
    
    def __init__(self) -> None:
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="SCORE: 0", fg="white", bg=THEME_COLOR, font=('Arial', 10))
        self.score_label.grid(column=1, row=0, sticky="ES") 

        self.canvas        = Canvas(width=300, height=250, bg='white')
        self.question_text = self.canvas.create_text(
            150,
            125,
            text='Question text!',
            fill=THEME_COLOR,
            font=('Arial', 20, 'italic'))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        true_image = PhotoImage(file='./quiz_app/images/true.png')
        self.true_button = Button(image=true_image, bg=THEME_COLOR, highlightthickness=0)
        self.true_button.grid(column=0, row=3)

        false_image = PhotoImage(file='./quiz_app/images/false.png')
        self.false_button = Button(image=false_image, bg=THEME_COLOR, highlightthickness=0)
        self.false_button.grid(column=1, row=3)

        self.window.mainloop()
        
    def right_answer():
        pass