from data import QData
from question import Question
from gamemaster import GameMaster

import tkinter as tk

def main():
    root = tk.Tk()
    root.title('Quiz Game')
    root.geometry('400x400')
    
    amount = 10
    cat = 'any'
    diff = 'any'
    type = 'any'
    
    gm = GameMaster(root, amount, cat, diff, type)
    
    root.mainloop()
    
if __name__ == '__main__':
    main()