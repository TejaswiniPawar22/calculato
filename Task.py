import tkinter as tk
import tkinter.messagebox
from tkinter.constants import SUNKEN

window = tk.Tk()
window.title('My calculator')
frame = tk.Frame(master=window, bg="white", padx=20)
frame.pack()

entry = tk.Entry(master=frame, relief=SUNKEN, borderwidth=3, width=30)
entry.grid(row=0, column=0, columnspan=4, ipady=2, pady=2)


# Define the myclick function to get the input from the user
def myclick(number):
    entry.insert(tk.END, number)


# Define an equal function to evaluate the value
def equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)  # Clear the entry box
        entry.insert(tk.END, str(result))  # Insert the result
    except Exception as e:
        tkinter.messagebox.showerror("Error", "Invalid Input")


# Create buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    if button == 'C':
        tk.Button(frame, text=button, padx=20, pady=20, command=lambda: entry.delete(0, tk.END)).grid(row=row_val,
                                                                                                      column=col_val)
    elif button == '=':
        tk.Button(frame, text=button, padx=20, pady=20, command=equal).grid(row=row_val, column=col_val)
    else:
        tk.Button(frame, text=button, padx=20, pady=20, command=lambda b=button: myclick(b)).grid(row=row_val,
                                                                                                  column=col_val)

    col_val += 1
    if col_val > 3:  # Move to next row after 4 columns
        col_val = 0
        row_val += 1

window.mainloop()

