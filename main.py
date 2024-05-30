import tkinter
import math
from playsound import playsound
import os

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
timer = ""


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    timer_label["text"] = "Timer"
    timer_label["fg"] = "black"
    global timer
    windows.after_cancel(timer)
    canvas.itemconfig(text_time, text=f"00:00")
    check_mark["text"] = ""


# ---------------------------- TIMER MECHANISM ------------------------------- #
def main_start():
    global REPS
    REPS = 0
    check_mark["text"] = ""
    timer_label["text"] = "Timer"
    start_timer()


def start_timer():
    global REPS
    REPS += 1

    if REPS % 8 == 0:
        timer_label["text"] = "BREAK"
        timer_label.config(fg=RED)
        check_mark["text"] = f"{check_mark['text']}✔"
        count_down(LONG_BREAK_MIN * 60)
        # study
    elif REPS % 2 == 0:
        timer_label["text"] = "BREAK"
        timer_label.config(fg=PINK)
        check_mark["text"] = f"{check_mark['text']}✔"
        count_down(SHORT_BREAK_MIN * 60)
        # study
    else:
        timer_label["text"] = "WORK"
        timer_label.config(fg="black")
        count_down(WORK_MIN * 60)
        # break


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec in range(0, 10):
        count_sec = f"0{count_sec}"

    canvas.itemconfig(text_time, text=f"{count_min}:{count_sec}")
    if count >= 1:
        global timer
        timer = windows.after(1000, count_down, count - 1)
    else:
        if REPS % 2 == 0:
            playsound(r"C:\Users\yerra\PycharmProjects\pomodoro-start\study_alarm.mp3")
        else:
            playsound(r"C:\Users\yerra\PycharmProjects\pomodoro-start\break_alarm.mp3")
        start_timer()


# ---------------------------- UI SETUP g------------------------------- #

windows = tkinter.Tk()
windows.title("POMODORO")
timer_label = tkinter.Label(text="Timer", font=(FONT_NAME, 30), bg=YELLOW, fg="black")
windows.config(padx=100, pady=100, bg=YELLOW)
timer_label.grid(column=2, row=1)
start_button = tkinter.Button(text="start", command=main_start)
canvas = tkinter.Canvas(width=206, height=224, bg=YELLOW, highlightthickness=0)
image_tomato = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=image_tomato)
text_time = canvas.create_text(107, 130, text="00:00", font=(FONT_NAME, 31, "bold"), fill="white")
canvas.grid(column=2, row=2)
check_mark = tkinter.Label(text="", fg="black", bg=YELLOW)
start_button.grid(column=1, row=3)

restart_button = tkinter.Button(text="reset", command=reset_timer)
restart_button.grid(column=3, row=3)
check_mark.grid(column=2, row=4)

windows.mainloop()
