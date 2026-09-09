

from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import requests

def update_b_label(event):
    code = base_combobox.get()
    name = currencies[code]
    b_label.config(text=name)

def update_b2_label(event):
    code = base2_combobox.get()
    name = currencies[code]
    b2_label.config(text=name)

def update_t_label(event):
    code = target_combobox.get()
    name = currencies[code]
    t_label.config(text=name)

def exchange():
    target_code = target_combobox.get()
    base_code = base_combobox.get()
    base2_code = base2_combobox.get()

    if target_code and base_code and base2_code:
        result_text = ""
        # Запрашиваем курсы для каждой базовой валюты
        for base_code_i in [base_code, base2_code]:
            try:
                response = requests.get(f'https://open.er-api.com/v6/latest/{base_code_i}')
                response.raise_for_status()
                data = response.json()

                if target_code in data['rates']:
                    exchange_rate = data['rates'][target_code]
                    base = currencies[base_code_i]
                    target = currencies[target_code]
                    result_text += f"Курс {exchange_rate:.1f} {target} за 1 {base}\n"
                else:
                    result_text += f"Валюта {target_code} не найдена для {base_code_i}\n"
            except Exception as e:
                result_text += f"Ошибка ({base_code_i}): {e}\n"

        mb.showinfo("Курсы обмена", result_text)
    else:
        mb.showwarning("Внимание", "Выберите коды всех валют")

# Словарь кодов валют и их полных названий
currencies = {
    "USD": "Американский доллар",
    "EUR": "Евро",
    "JPY": "Японская йена",
    "GBP": "Британский фунт стерлингов",
    "AUD": "Австралийский доллар",
    "CAD": "Канадский доллар",
    "CHF": "Швейцарский франк",
    "CNY": "Китайский юань",
    "RUB": "Российский рубль",
    "KZT": "Казахстанский тенге",
    "UZS": "Узбекский сум"
}

# Создание графического интерфейса
window = Tk()
window.title("Курс обмена валюты")
window.geometry("360x420")

Label(text="Базовая валюта:").pack(padx=10, pady=5)
base_combobox = ttk.Combobox(values=list(currencies.keys()))
base_combobox.pack(padx=10, pady=5)
base_combobox.bind("<<ComboboxSelected>>", update_b_label)

b_label = ttk.Label()
b_label.pack(padx=10, pady=5)

Label(text="Вторая базовая валюта:").pack(padx=10, pady=5)
base2_combobox = ttk.Combobox(values=list(currencies.keys()))
base2_combobox.pack(padx=10, pady=5)
base2_combobox.bind("<<ComboboxSelected>>", update_b2_label)

b2_label = ttk.Label()
b2_label.pack(padx=10, pady=5)

Label(text="Целевая валюта:").pack(padx=10, pady=5)
target_combobox = ttk.Combobox(values=list(currencies.keys()))
target_combobox.pack(padx=10, pady=5)
target_combobox.bind("<<ComboboxSelected>>", update_t_label)

t_label = ttk.Label()
t_label.pack(padx=10, pady=5)

Button(text="Получить курс обмена", command=exchange).pack(padx=10, pady=10)

window.mainloop()



