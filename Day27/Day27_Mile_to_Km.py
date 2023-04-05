from tkinter import *

window = Tk()
window.title("Miles - Kilometers Converter")
window.minsize(width=400, height=100)


#Labels

top_left_space = Label(text="")
top_left_space.grid(row=0, column=0)
top_left_space.config(padx=80, pady=8)

miles = Label(text="Miles")
miles.grid(row=1, column=2)

is_equal_to = Label(text="is equal to")
is_equal_to.grid(row=2, column=0)

answer = Label(text="0")
answer.grid(row=2, column=1)

km = Label(text="Km")
km.grid(row=2, column=2)

bottom_left_space = Label(text="")
bottom_left_space.grid(row=3, column=0)
bottom_left_space.config(padx=80, pady=8)

#Input

input = Entry(width=10)
input.grid(row=1, column=1)

#Button
def calculate():
        mile = input.get()
        kilometer = round(float(mile) * 1.609344, 2)
        answer.config(text=kilometer)


calculate_button = Button(text="Calculate", command=calculate)
calculate_button.grid(row=3, column=1)













window.mainloop()