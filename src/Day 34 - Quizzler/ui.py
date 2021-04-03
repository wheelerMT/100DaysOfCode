import tkinter
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        # Generate window
        self.window = tkinter.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Score text
        self.score_label = tkinter.Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)

        # Question area
        self.question_area = tkinter.Canvas(width=300, height=250)
        self.question_text = self.question_area.create_text(150, 125, width=280,
                                                            text="Some Question Text",
                                                            font=("Arial", 20, "italic"))
        self.question_area.grid(row=1, column=0, columnspan=2, pady=50)

        # Buttons
        true_image = tkinter.PhotoImage(file="images/true.png")
        self.true_button = tkinter.Button(image=true_image, highlightthickness=0, bg=THEME_COLOR,
                                          command=self.true_pressed)
        self.true_button.grid(row=2, column=0)

        false_image = tkinter.PhotoImage(file="images/false.png")
        self.false_button = tkinter.Button(image=false_image, highlightthickness=0, bg=THEME_COLOR,
                                           command=self.false_pressed)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.question_area.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.question_area.itemconfig(self.question_text, text=q_text)
        else:
            self.question_area.itemconfig(self.question_text, text="You've completed the quiz!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_correct):
        if is_correct:
            self.question_area.config(bg="green")
        else:
            self.question_area.config(bg="red")

        self.window.after(1000, self.get_next_question)
