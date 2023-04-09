from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
timer = None 

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global REPS
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, "bold"))
    check_mark.config(text="")
    REPS = 0
    
# ---------------------------- POP-UP------------------------------- # 
def open_popup():
    top= Toplevel(window)
    top.geometry("250x150")
    top.title("Pomodoro Alert")
    Label(top, text= "Time is up!", font=('Mistral 18 bold')).place(x=50,y=40)

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global REPS
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    REPS += 1
    if REPS == 0:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)
    elif REPS % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=RED)
    elif REPS % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global REPS
    minutes = count // 60
    seconds = count % 60
    if len(str(seconds)) == 1:
        seconds = f"0{seconds}"
    clock = f"{minutes}:{seconds}"
    canvas.itemconfig(timer_text, text=clock)
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        open_popup()
        start_timer()
        check_number = REPS // 2
        output = ""
        for i in range(REPS // 2):
            output += "✓"
        check_mark.config(text=output)
        
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=150, pady=100, bg=YELLOW)



canvas = Canvas(width= 200, height= 224, bg=YELLOW, highlightthickness=0)
tomato_png = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_png)
timer_text = canvas.create_text(100, 130, text="25:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=2,column=2)

start_button = Button(text="Start", command= start_timer)
start_button.grid(row=3, column=1)
reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(row=3, column=3)
timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, "bold"))
timer_label.grid(row=1, column=2)
check_mark = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, "bold"))
check_mark.grid(row=4, column=2)




window.mainloop()