from tkinter import *

# Create window and config
window = Tk()
window.title("Miles to KM Converter")
window.minsize(width=300, height=300)
window.config(padx=50, pady=100)

# Define function
def convert():
    miles = float(input_box.get())
    kms = round(miles * 1.60934, 2)
    converted_label.config(text=kms)

# Input field
input_box = Entry(width=10)
input_box.insert(END, string="0")
input_box.grid(column=1, row=0)

# Mile Label
mile_label = Label(text="Miles")
mile_label.grid(column=2, row=0)

# Equal to label
equals_label = Label(text="is equal to")
equals_label.grid(column=0, row=1)

# Converted label
converted_label = Label(text="0")
converted_label.grid(column=1, row=1)

# KM label
km_label = Label(text="KM")
km_label.grid(column=2, row=1)

# Calculate button
calculate_button = Button(text="Calculate", command=convert)
calculate_button.grid(column=1, row=2)

window.mainloop()