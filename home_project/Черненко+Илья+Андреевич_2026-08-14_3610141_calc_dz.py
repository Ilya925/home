import os

file_path = 'calculations.txt'


def add(x, y):
    res1 = x + y
    return round(res1, 2)


def subtract(x, y):
    res2 = x - y
    return round(res2, 2)


def multiply(x, y):
    res3 = x * y
    return round(res3, 2)


def divide(x, y):
    if y == 0:
        return 'Ошибка: Деление на ноль'
    res4 = x / y
    return round(res4, 2)


def log(result):
    with open(file_path, 'a', encoding='utf-8') as file:
        file.write(result + '\n')


def history():
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            hist = file.read()
            if hist.strip():
                print(f'--- История вычислений ---\n{hist}')
            else:
                print('История пуста.')
    else:
        print('Вычислений пока не было.')


print('Выберите операцию:')
print('1. Сложение')
print('2. Вычитание')
print('3. Умножение')
print('4. Деление')
print('5. Просмотр истории вычислений')
print('6. Выход из программы')

while True:
    choice = input('Введите номер операции 1/2/3/4/5/6: ')
    if choice == '5':
        history()
        continue

    if not (choice.isdigit() and 1 <= int(choice) <= 6):
        print('Неверный выбор. Введите число от 1 до 6.')
        continue

    if choice == '6':
        print('Программа завершена')
        break

    num1 = float(input('Введите первое число: '))
    num2 = float(input('Введите второе число: '))

    if choice == '1':
        r = f'Результат: {num1} + {num2} = {add(num1, num2)}'
    elif choice == '2':
        r = f'Результат: {num1} - {num2} = {subtract(num1, num2)}'
    elif choice == '3':
        r = f'Результат: {num1} * {num2} = {multiply(num1, num2)}'
    elif choice == '4':
        r = f'Результат: {num1} / {num2} = {divide(num1, num2)}'
    print(r)
    log(r)