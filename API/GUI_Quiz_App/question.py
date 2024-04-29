import tkinter as tk

class Question:
    def __init__(self, master, question, answers):
        self.master = master
        self.question = question
        self.answers = answers

        self.label = tk.Label(master, text=question)
        self.label.pack()

        self.buttons = []
        for answer in answers:
            button = tk.Button(master, text=answer, command=self.on_button_click)
            button.pack()
            self.buttons.append(button)
            button.focus_set()

    def on_button_click(self):
        button = self.master.focus_get()
        if isinstance(button, tk.Button) and 'text' in button.keys():
            answer = button['text']
            if self.check_answer(answer):
                button.config(bg='green')
            else:
                button.config(bg='red')
            self.master.after(1000, self.destroy)
            self.master.after(1000, self.master.next_question)
        else:
            print("Focused widget is not a button or does not have 'text'.")
        
    def destroy(self):
        self.label.destroy()
        for button in self.buttons:
            button.destroy()
    
    def check_answer(self, answer):
        if answer == self.correct_answer:
            return True
        return False
    
    def set_correct_answer(self, correct_answer):
        self.correct_answer = correct_answer
        
    def get_correct_answer(self):
        return self.correct_answer
    
    def get_question(self):
        return self.question