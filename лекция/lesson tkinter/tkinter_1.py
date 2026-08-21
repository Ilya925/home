from tkinter0_2 import Tk, Label, Entry, Button, messagebox as mb

from requests import delete


def calculate(operation):
    # Получаем значения из полей
    values = [e1.get(), e2.get(), e3.get()]

    # Пробуем преобразовать в float, собираем ошибки
    numbers = []
    for i, v in enumerate(values, start=1):
        try:
            num = float(v)
            numbers.append(num)
        except ValueError:
            mb.showerror("Ошибка", f"В поле {i} должно быть число")
            return

    if operation == "sum":
        result = sum(numbers)
        expr = f"{numbers[0]} + {numbers[1]} + {numbers[2]} = {result:.2f}"
    elif operation == "mul":
        result = numbers[0] * numbers[1] * numbers[2]
        expr = f"{numbers[0]} * {numbers[1]} * {numbers[2]} = {result:.2f}"
    elif operation == delete(values):
        result = delete()
    else:
        return

    m1['text'] = expr


window = Tk()
window.title("Калькулятор трёх чисел")

m = Label(
    text="Введи три числа (можно дробные) и нажми кнопку для вычисления",
    height=3,
    justify="center"
)
m.pack()

e1 = Entry(width=20)
e1.pack(pady=2)
e2 = Entry(width=20)
e2.pack(pady=2)
e3 = Entry(width=20)
e3.pack(pady=2)

b_sum = Button(text="Сложить три числа", command=lambda: calculate("sum"))
b_sum.pack()

b_mul = Button(text="Умножить три числа", command=lambda: calculate("mul"))
b_mul.pack()

b = Button(text="Очистить", command=lambda: calculate("mul"))
b.pack()

m1 = Label(height=3, font=("Arial", 12), fg="#333333")
m1.pack()

window.mainloop()
