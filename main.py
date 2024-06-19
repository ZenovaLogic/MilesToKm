from tkinter import *


def button_clicked():
    miles = float(miles_input.get())
    km = miles * 1.609
    km_value.config(text=f"{km}")


# Clear the input box when focussed, if value is 0
def clear_zero(event):
    if event.widget.get() == '0':
        event.widget.delete(0, END)


window = Tk()
window.title("Miles to Km Converter")
window.config(padx=40, pady=20)

miles_input = Entry(width=10)
miles_input.insert(END, string="0")
miles_input.bind("<FocusIn>", clear_zero)  # Clear when focussed (if 0)
miles_label = Label(text="Miles")
equal_label = Label(text="is equal to ")
km_value = Label(text="0")
km_label = Label(text="Km")
button = Button(text="Calculate", command=button_clicked)

# Place the widgets on a grid
miles_input.grid(column=1, row=0)
miles_label.grid(column=2, row=0)
equal_label.grid(column=0, row=1)
km_value.grid(column=1, row=1)
km_label.grid(column=2, row=1)
button.grid(column=1, row=2)

window.mainloop()
