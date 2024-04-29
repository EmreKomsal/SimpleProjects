from tkinter import *
import time
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 4

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(countdown)
    canvas.itemconfig(timer_text, text="00:00")
    timerLabel.config(text="Timer", fg=GREEN)
    chekmarkLabel.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    reps += 1
    if reps % 8 == 0:
        countdown(long_break_sec)
        timerLabel.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        countdown(short_break_sec)
        timerLabel.config(text="Break", fg=PINK)
    else:
        countdown(work_sec)
        timerLabel.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def countdown(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")    
    if count > 0:
        window.after(1000, countdown, count - 1)
    else:
        window.after(1000, countdown, count)
        mark = ""
        for _ in range(math.floor(reps/2)):
            mark += "✔"
        chekmarkLabel.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="/Users/ekomsal/Projects/PythonProjects/SimpleProjects/GUI/pomodoro/tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

timerLabel = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
timerLabel.grid(row=0, column=1)

startButton = Button(text="Start", highlightthickness=0, bg=YELLOW, fg=GREEN, command=start_timer)
startButton.config(padx=10, pady=5)
startButton.grid(row=2, column=0, padx=10)

resetButton = Button(text="Reset", highlightthickness=0, bg=YELLOW, fg=GREEN)
resetButton.config(padx=10, pady=5)
resetButton.grid(row=2, column=2, padx=10)

chekmarkLabel = Label(text="✔", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
chekmarkLabel.config(padx=10, pady=5)
chekmarkLabel.grid(row=3, column=1, pady=10)



window.mainloop()