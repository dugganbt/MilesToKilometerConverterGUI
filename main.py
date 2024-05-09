from tkinter import *

""" 
Author: Brian Duggan
This is an exercise in GUI creation using Tkinter and is from the course: 100 Days of Code: the Complete Python Bootcamp by 
Dr. Angela. 

The program is a simple converter from miles to kilometers.
"""

# Creating a GUI window
window = Tk()
window.title("Miles to Km Converter")
window.config(padx=20, pady=20)

# Input miles box
input = Entry(width=10)
input.grid(column=1, row=0)
input.insert(0, 0)

# Miles label
miles = Label(text="Miles")
miles.grid(column=2, row=0)

# is equal to label
is_equal_to_text = Label(text="is equal to")
is_equal_to_text.grid(column=0, row=1)

# answer in km text
answer_text = Label(text=0)
answer_text.grid(column=1, row=1)

# Miles label
miles = Label(text="Km")
miles.grid(column=2, row=1)


# Calculate function
def calculate_button_clicked():
    """Sets the answer text to the converted miles"""
    kilometers = round(float(input.get()) * 1.6, ndigits=2)
    answer_text.config(text=kilometers)


# Calculate button
miles = Button(text="Calculate", command=calculate_button_clicked)
miles.grid(column=1, row=2)

window.mainloop()
