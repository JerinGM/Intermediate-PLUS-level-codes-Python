THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.qb = quiz_brain
        self.window = Tk()
        self.window.title("Quiz Game")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.label = Label(text="Score: 0", fg="white", bg=THEME_COLOR )
        self.label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.text = self.canvas.create_text(150, 126, text="", fill="black", font=("Ariel", 20, "italic"), width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)

        falsebuttonimage = PhotoImage(file="./images/false.png")
        self.falsebutton = Button(image=falsebuttonimage, highlightthickness=0, command=self.wrong_answer)
        self.falsebutton.grid(row=2, column=0)

        truebuttonimage = PhotoImage(file="./images/true.png")
        self.truebutton = Button(image=truebuttonimage, highlightthickness=0, command=self.correct_answer)
        self.truebutton.grid(row=2, column=1)

        self.next_question()

        self.window.mainloop()

    def next_question(self):
        self.canvas.config(bg="white")
        if self.qb.still_has_questions():
            self.label.config(text=f"Score : {self.qb.score}")
            qtext = self.qb.next_question()
            self.canvas.itemconfig(self.text, text=qtext)
        else:
            self.canvas.itemconfig(self.text, text="Quiz is Over now")
            self.truebutton.config(state="disabled")
            self.falsebutton.config(state="disabled")

    def correct_answer(self):
        is_right = self.qb.check_answer("True")
        self.give_feedback(is_right)

    def wrong_answer(self):
        is_right = self.qb.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(500, self.next_question)
