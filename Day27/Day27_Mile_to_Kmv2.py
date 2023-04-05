from tkinter import *

window = Tk()
window.title("Miles - Kilometers Converter")
window.minsize(width=400, height=100)

#Radiobutton
def radio_used():
    if radio_state.get() == 1:
        miles.grid(row=1, column=2)
        km.grid(row=2, column=2)
    #Function for Mile to Km
        def calculate():
            mile = input.get()
            kilometer = round(float(mile) * 1.609344, 2)
            answer.config(text=kilometer)
        
#Labels for Km to Mile 
    if radio_state.get() == 2:
        miles.grid(row=2, column=2)
        km.grid(row=1, column=2)

    #Function for Km to Mile
        def calculate():
            kilometer = input.get()
            mile = round(float(kilometer) / 1.609344, 2)
            answer.config(text=mile)
    calculate_button = Button(text="Calculate", command=calculate)
    calculate_button.grid(row=3, column=1)
    
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Mile to Kilometer", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Kilometer to Mile", value=2, variable=radio_state, command=radio_used)
radiobutton1.grid(row=4, column=1)
radiobutton2.grid(row=5, column=1)
radiobutton1.select()

#Labels 
top_left_space = Label(text="")
top_left_space.grid(row=0, column=0)
top_left_space.config(padx=80, pady=8)

is_equal_to = Label(text="is equal to")
is_equal_to.grid(row=2, column=0)

answer = Label(text="0")
answer.grid(row=2, column=1)

bottom_left_space = Label(text="")
bottom_left_space.grid(row=3, column=0)
bottom_left_space.config(padx=80, pady=8)

miles = Label(text="Miles")
miles.grid(row=1, column=2)

km = Label(text="Km")
km.grid(row=2, column=2)
#Labels for Mile to Km



#Input
input = Entry(width=10)
input.grid(row=1, column=1)

#First Start Button
def calculate():
    mile = input.get()
    kilometer = round(int(mile) * 1.609344, 2)
    answer.config(text=kilometer)
calculate_button = Button(text="Calculate", command=calculate)
calculate_button.grid(row=3, column=1)
    
window.mainloop()