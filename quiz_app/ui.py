from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:
    
    def __init__(self, quiz_brain: QuizBrain) -> None:
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="SCORE: 0", fg="white", bg=THEME_COLOR, font=('Arial', 10))
        self.score_label.grid(column=1, row=0, sticky="ES") 

        self.canvas        = Canvas(width=300, height=250, bg='white')
        self.question_text = self.canvas.create_text(
            150,
            125,
            width= 280,
            text='Question text!',
            fill=THEME_COLOR,
            font=('Arial', 20, 'italic'))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        true_image = PhotoImage(file='./quiz_app/images/true.png')
        self.true_button = Button(image=true_image, bg=THEME_COLOR, highlightthickness=0, command=self.select_true)
        self.true_button.grid(column=0, row=3)

        false_image = PhotoImage(file='./quiz_app/images/false.png')
        self.false_button = Button(image=false_image, bg=THEME_COLOR, highlightthickness=0, command=self.select_false)
        self.false_button.grid(column=1, row=3)

        self.get_next_question()

        self.window.mainloop()
        

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.score_label.config(text=f'Score: {self.quiz.score}')
            self.canvas.config(bg='white')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.config(bg='white')
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')

            self.canvas.itemconfig(self.question_text, text='THE QUIZ IS OVER!')

            

    # selcting the right button
    def select_true(self):
        self.give_user_feedback(self.quiz.check_answer('True'))
        # self.canvas.itemconfig(self.score_label, text=f'Score: {score}')

    
    # selecting the wrong button
    def select_false(self):
        self.give_user_feedback(self.quiz.check_answer('False'))
        # self.canvas.itemconfig(self.score_label, text=f'Score: {score}')


    def give_user_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        
        self.window.after(1000, self.get_next_question)