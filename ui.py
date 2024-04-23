from tkinter import *
THEME_COLOR = "#375362"
from quiz_brain import QuizBrain
class QuizeInterface:

    def __init__(self,quize_brain:QuizBrain):
        self.quiz=quize_brain
#-----------------------------------UI----------------------------------------------------------------------#

        self.window=Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

#------------------Label the score at the corner---------------------------------------------------------------------#

        self.score_label=Label(text="Score:0/10", font=("",15),fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

#---------------Canvas position height and width and also question_text put it down here---------------------------#

        self.canvas=Canvas(height=250 , width=300, bg="white")
        self.question_text=self.canvas.create_text(150,125,text="Question Text",
                                                   fill=THEME_COLOR,
                                                   width=270,
                                                   font=("Arial", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2,pady=50)

#------------Importing false.png pic and make it form of button that work on click to change the state------------------#

        self.false_img=PhotoImage(file="images/false.png")
        self.false_button=Button(image=self.false_img, command=self.false_answer)
        self.false_button.grid(column=1, row=3)

#--------------Importing True.png image and make the in th form of btton to change it state ------------------------#

        self.true_img=PhotoImage(file="images/true.png")
        self.true_button=Button(image=self.true_img, command=self.true_answer)
        self.true_button.grid(column=0,row=3)
        self.get_next_question()


        self.window.mainloop()

#-----------------Definig the next question in quiz--------------------------------------------------------------#
    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}/10")
            q_text=self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
#-----------Defining the method to call check_answer from quiz_brain-----------------------------------#

    def true_answer(self):
        is_right=self.quiz.check_answer("True")
        self.give_feedback(is_right)


    def false_answer(self):
        is_right=self.quiz.check_answer("False")
        self.give_feedback(is_right)
    def give_feedback(self, is_right):

        self.window.after(3000,func=self.get_next_question)

        if is_right==True:
            self.canvas.config(bg="green")
        elif is_right==False:
            self.canvas.config(bg="red")




