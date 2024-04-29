import tkinter as tk
from data import QData

class UI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Quiz App")
        self.window.geometry("500x500")
        
        self.label = tk.Label(self.window, text="Welcome to the Quiz App!")
        self.label.grid(row= 0, column= 1, columnspan= 3)
        
        #Categories and difficulties
        
        self.categories = {'Any Category': 'any', 'General Knowledge': 9, 'Entertainment: Books': 10, 'Entertainment: Film': 11, 'Entertainment: Music': 12, 'Entertainment: Musicals & Theatres': 13, 'Entertainment: Television': 14, 'Entertainment: Video Games': 15, 'Entertainment: Board Games': 16, 'Science & Nature': 17, 'Science: Computers': 18, 'Science: Mathematics': 19, 'Mythology': 20, 'Sports': 21, 'Geography': 22, 'History': 23, 'Politics': 24, 'Art': 25, 'Celebrities': 26, 'Animals': 27, 'Vehicles': 28, 'Entertainment: Comics': 29, 'Science: Gadgets': 30, 'Entertainment: Japanese Anime & Manga': 31, 'Entertainment: Cartoon & Animations': 32}
        self.difficulties = {'Any Difficulty': 'any', 'Easy': 'easy', 'Medium': 'medium', 'Hard': 'hard'}
        
        self.num_questions_label = tk.Label(self.window, text="Number of Questions:")
        self.num_questions = tk.Entry(self.window)
        
        self.cat_label = tk.Label(self.window, text="Category:")
        self.cat = tk.StringVar(self.window)
        self.cat.set('Any Category')
        self.cat_menu = tk.OptionMenu(self.window, self.cat, *self.categories.keys())
        
        self.diff_label = tk.Label(self.window, text="Difficulty:")
        self.diff = tk.StringVar(self.window)
        self.diff.set('Any Difficulty')
        self.diff_menu = tk.OptionMenu(self.window, self.diff, *self.difficulties.keys())
        
        self.start_button = tk.Button(self.window, text="Start", command=self.start)
        
        self.num_questions_label.grid(row= 2, column= 1)
        self.num_questions.grid(row= 2, column= 2)
        self.cat_label.grid(row= 3, column= 1)
        self.cat_menu.grid(row= 3, column= 2)
        self.diff_label.grid(row= 4, column= 1)
        self.diff_menu.grid(row= 4, column= 2)
        self.start_button.grid(row= 5, column= 1, columnspan= 2)
        
        self.window.mainloop()
        
            
    def start(self):
        amount = self.num_questions.get()
        cat = self.categories[self.cat.get()]
        diff = self.difficulties[self.diff.get()]
        
        data = QData(amount, cat, diff)
        questions = data.get_questions()
        print(questions)
        