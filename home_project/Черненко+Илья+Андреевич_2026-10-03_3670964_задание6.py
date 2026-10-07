import tkinter as tk
from tkinter import ttk, messagebox
import requests

crypto_ids = {
    'BTC': 'bitcoin',
    'ETH': 'ethereum',
    'TRUMP': 'official-trump',
    'USDT': 'tether',
    'SOL': 'solana'
}


def get_crypto_rate(symbol):
    try:
        url = f'https://api.coingecko.com/api/v3/simple/price?ids={crypto_ids[symbol]}&vs_currencies=usd'
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        # В ответе CoinGecko ключ — это ID монеты, а не тикер. Нужно брать по crypto_ids[symbol]
        return data[crypto_ids[symbol]]['usd']
    except requests.exceptions.RequestException as e:
        messagebox.showerror('Ошибка сети', f'Не удалось получить данные: {e}')
        return None
    except KeyError as e:
        messagebox.showerror('Ошибка данных', f'Неожиданный формат ответа API: {e}')
        return None


def update_label():
    symbol = combo_box.get()
    if not symbol:
        messagebox.showwarning('Внимание', 'Выберите криптовалюту из списка.')
        return
    rate = get_crypto_rate(symbol)
    if rate is not None:
        label_result.config(text=f'Курс: {rate:.2f} USD')
    else:
        label_result.config(text='Ошибка получения курса')


root = tk.Tk()
root.title('Курсы криптовалют')
root.geometry('300x150')

crypto_display = {
    'BTC': 'Bitcoin',
    'ETH': 'Ethereum',
    'TRUMP': 'official-trump',
    'USDT': 'Tether',
    'SOL': 'Solana'
}

combo_box = ttk.Combobox(root, values=list(crypto_display.keys()), state='readonly')
combo_box.current(0)
combo_box.pack(pady=10)

button_get_rate = tk.Button(root, text='Получить курс', command=update_label)
button_get_rate.pack(pady=5)

label_result = tk.Label(root, text='', font=('Helvetica', 12), width=20, anchor='w')
label_result.pack(pady=10)

root.mainloop()
