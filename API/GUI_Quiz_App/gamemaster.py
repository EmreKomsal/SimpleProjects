import tkinter as tk
from data import QData
from question import Question


class GameMaster:
    def __init__(self, master, amount, cat, diff, type):
        self.master = master
        self.amount = amount
        self.cat = cat
        self.diff = diff
        self.type = type
        
        self.qdata = QData(amount, cat, diff, type)
        self.questions = self.qdata.get_questions()
        self.current_question = 0
        
        self.show_question()
        
    def show_question(self):
        question = self.questions[self.current_question]
        answers = self.qdata.get_answers(question)
        correct_answer = self.qdata.get_correct_answer(question)
        
        self.question = Question(self.master, question['question'], answers)
        self.question.set_correct_answer(correct_answer)
        
    def next_question(self):
        self.current_question += 1
        if self.current_question < self.amount:
            self.show_question()
        else:
            self.master.destroy()
            
    def get_questions(self):
        return self.questions
    
    def get_current_question(self):
        return self.current_question
        
    
        
        
        
        

