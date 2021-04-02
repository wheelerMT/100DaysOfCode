from tkinter import *

FONT = ("Arial", 16, "normal")
def button_clicked():
    miles_conversion_label["text"] = round(float(input_field.get()) * 1.609, 2)


# Window
window = Tk()
window.title("Miles to Km converter")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)

# Entry
input_field = Entry(width=10)
input_field.grid(row=0, column=1)

# Labels
miles_label = Label(text="Miles", font=FONT)
miles_label.grid(row=0, column=2)

is_eq_to_label = Label(text="is equal to", font=FONT)
is_eq_to_label.grid(row=1, column=0)

miles_conversion_label = Label(text="0", font=FONT)
miles_conversion_label.grid(row=1, column=1)

km_label = Label(text="Km", font=FONT)
km_label.grid(row=1, column=2)

# Button
calc_button = Button(text="Calculate", command=button_clicked)
calc_button.grid(row=2, column=1)


window.mainloop()
