import numpy as np


def get_input_method():
    while True:
        print("Выберите метод ввода исходных данных:")
        print("1. Ввод с клавиатуры")
        print("2. Чтение из файла")
        print("3. Выбор функции")
        choice = input("Введите номер метода (1/2/3): ")

        if choice in ['1', '2', '3']:
            return int(choice)
        else:
            print("Неверный ввод. Введите 1, 2 или 3.")


def input_from_keyboard():
    points = int(input("Введите количество точек: "))
    x = []
    y = []
    for i in range(points):
        x.append(float(input(f"x[{i}]: ")))
        y.append(float(input(f"y[{i}]: ")))
    return np.array(x), np.array(y)


def input_from_file():
    while True:
        filename = input("Введите имя файла: ")

        try:
            with open(filename, 'r') as file:
                lines = file.readlines()
                x = np.array([float(val) for val in lines[0].split()])
                y = np.array([float(val) for val in lines[1].split()])
            return x, y
        except FileNotFoundError:
            print("Файл не найден. Попробуйте снова.")


def select_function():
    functions = {
        1: np.sin,
        2: np.cos
    }
    while True:
        print("Выберите функцию:")
        print("1. sin(x)")
        print("2. cos(x)")
        choice = input("Введите номер функции (1/2): ")

        if choice in ['1', '2']:
            choice = int(choice)
            func = functions[choice]
            break
        else:
            print("Неверный ввод. Пожалуйста, введите 1 или 2.")

    while True:
        try:
            a = float(input("Введите начало интервала: "))
            b = float(input("Введите конец интервала: "))
            points = int(input("Введите количество точек: "))
            x = np.linspace(a, b, points)
            y = func(x)
            return x, y
        except ValueError:
            print("Неверный ввод. Пожалуйста, введите числовые значения.")