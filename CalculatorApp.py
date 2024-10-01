import tkinter as tk
from math import sqrt, log

# Create the main window
window = tk.Tk()
window.title("Advanced Calculator")

# Calculator logic
def calculate(expression):
    try:
        result = eval(expression)
        display.delete(0, tk.END)
        display.insert(tk.END, str(result))
    except Exception as e:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")

# Create the display
display = tk.Entry(window, width=40, borderwidth=5)
display.grid(row=0, column=0, columnspan=5)

# Button click function
def button_click(value):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(tk.END, current + value)

def clear_display():
    display.delete(0, tk.END)

# Buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3), ('sqrt', 1, 4),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3), ('log', 2, 4),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3), ('%', 3, 4),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3), ('C', 4, 4)
]

for (text, row, col) in buttons:
    tk.Button(window, text=text, command=lambda t=text: button_click(t)).grid(row=row, column=col)

tk.Button(window, text='Clear', command=clear_display).grid(row=5, column=0, columnspan=5)
tk.Button(window, text='=', command=lambda: calculate(display.get())).grid(row=4, column=2)

window.mainloop()
