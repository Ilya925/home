from tkinter import *

from tkinter import messagebox as mb


#import tkinter as tk

root = Tk()
root.title("Калькулятор")
root.geometry("400x600")
root.configure(bg="#C9F7FC")

expression = ""

def button_click(item):
    global expression
    if item == "C":
        expression = ""
    else:
        if item in "+-*/" and expression and expression[-1] in "+-*/":
            expression = expression[:-1] + item
        else:
            expression += str(item)
    entry.delete(0, END)
    entry.insert(0, expression)

def calculate():
    global expression
    try:
        result = eval(expression)
        result = round(result, 2)
        if result == int(result):
            result = int(result)
        expression = str(result)
        entry.delete(0, END)
        entry.insert(0, str(result))
    except Exception:
        entry.delete(0, END)
        entry.insert(0, "Error")
        expression = ""


entry = Entry(root, font=("Arial", 20), justify="right", width=20)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    'C'
]

row_val = 1
col_val = 0

for btn_text in buttons:
    if btn_text == "=":
        cmd = calculate
    else:
        cmd = lambda x=btn_text: button_click(x)

    button = Button(
        root,
        text=btn_text,
        font=("Arial", 20),
        width=5,
        height=2,
        command=cmd
    )
    button.grid(row=row_val, column=col_val, padx=5, pady=5)

    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

root.mainloop()
