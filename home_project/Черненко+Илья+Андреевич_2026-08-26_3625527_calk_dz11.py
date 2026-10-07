from pathlib import Path
from tkinter import Tk, Button, Label, Entry, messagebox, PhotoImage

W, H = 380, 220


def calc_summ():
    try:        # Получаем и конвертируем значения
        num1 = float(value1.get())
        num2 = float(value2.get())
        num3 = float(value3.get())
        res = num1 + num2 + num3
        result.config(text=f'Результат: {num1} + {num2} + {num3} = {res}',
                      bg='#274DEA')
    except ValueError:
        messagebox.showerror('Ошибка ввода', 'Прошу вводить корректные числа!')


def calc_prod():
    try:
        # Получаем и конвертируем значения
        num1 = float(value1.get())
        num2 = float(value2.get())
        num3 = float(value3.get())
        res2 = num1 * num2 * num3
        result.config(text=f'Результат: {num1} * {num2} * {num3} = {res2}',
                      bg='#274DEA')
    except ValueError:
        messagebox.showerror('Ошибка ввода', 'Прошу вводить корректные числа!')


root = Tk()
root.title('Калькулятор')
root.geometry(f'{W}x{H}')
root.resizable(False, False)

icon_path = Path('calc.png')

if icon_path.exists():
    img = PhotoImage(file=icon_path)
    root.iconphoto(True, img)
else:
    # messagebox.showerror('Ошибка файла', 'Файл иконки не найден')
    print('Иконка не найдена и используется стандартная')

Label(text='Введите три числа ниже и выберите кнопку для вычисления').pack()
value1 = Entry()
value1.pack(pady=(5, 0), padx=5)
value1.configure(bg='#EBFFDC')
value2 = Entry()
value2.pack(pady=(5, 0), padx=5)
value2.configure(bg='#EBFFDC')
value3 = Entry()
value3.pack(pady=(5, 0), padx=5)
value3.configure(bg='#EBFFDC')
Button(text='Сложить три числа', command=calc_summ).pack(pady=5)
Button(text='Умножить три числа', command=calc_prod).pack(pady=5)

result = Label(font=('Arial', 12, 'bold'))
result.pack(pady=(10, 0))

root.mainloop()
