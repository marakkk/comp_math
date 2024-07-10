import math
import numpy as np
import matplotlib.pyplot as plt


# Линейная функция: phi(x) = ax + b
def linear(x, a, b):
    return a * x + b


# Степенная функция: phi(x) = ax^b
def power(x, a, b):
    return a * (x ** b)


# Экспоненциальная функция: phi(x) = ae^(bx)
def exponential(x, a, b):
    return a * (x ** b)


# Логарифмическая функция: phi(x) = aln(x) + b
def logarithmic(x, a, b):
    try:
        return a * math.log(x) + b
    except ValueError:
        print("Использованы недопустимые значения")


# Полиномиальная функция второй степени: phi(x) = ax^2 + bx + c
def quadratic(x, a, b, c):
    return a * (x ** 2) + b * x + c


# Полиномиальная функция третьей степени: phi(x) = ax^3 + bx^2 + cx + d
def cubic(x, a, b, c, d):
    return a * (x ** 3) + b * (x ** 2) + c * x + d


def quadr(x, a, b, c, d, e):
    return a * (x ** 4) + b * (x ** 3) + c * (x ** 2) + d * x + e


def read_data_from_file(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        if len(lines) != 2:
            print("Ошибка: Файл должен содержать ровно две строки с данными.")
            return [], []

        x = [float(item) for item in lines[0].split()]
        y = [float(item) for item in lines[1].split()]

    return x, y


def input_data_from_console():
    while True:
        try:
            x = []
            y = []
            n = int(input("Введите количество точек (от 8 до 12): "))
            xi = [float(item) for item in input(f"Введите координаты x: ").split()]
            yi = [float(item) for item in input(f"Введите координаты y: ").split()]

            if len(xi) != n or len(yi) != n:
                print(f"Ошибка: Нужно ввести {n} координат в каждом измерении.")
                continue

            x.extend(xi)
            y.extend(yi)
            return x, y

        except ValueError:
            print("Ошибка при вводе данных, попробуйте еще раз")


#линейная аппроксимация
def linear_approximation(x, y, linear_func):
    SX: float = sum(x)
    SXX: float = sum([p ** 2 for p in x])
    SY: float = sum(y)
    SXY: float = sum([x[i] * y[i] for i in range(len(x))])
    delta = SXX * len(x) - SX * SX
    delta1 = SXY * len(x) - SX * SY
    delta2 = SXX * SY - SX * SXY

    a = delta1 / delta
    b = delta2 / delta
    func = lambda x: linear_func(x, a, b)
    return func, a, b


#полиномиальная функция второй степени
def polynomial_approximation_2(x, y, quadratic_func):
    n = len(x)
    SX = sum(x)
    SX2 = sum([p ** 2 for p in x])
    SX3 = sum([p ** 3 for p in x])
    SX4 = sum([p ** 4 for p in x])
    SY = sum(y)
    SXY = sum([x[i] * y[i] for i in range(n)])
    SX2Y = sum([x[i] * x[i] * y[i] for i in range(n)])

    x1 = np.array([[n, SX, SX2], [SX, SX2, SX3], [SX2, SX3, SX4]])

    y1 = np.array([SY, SXY, SX2Y])
    a = np.linalg.solve(x1, y1)

    func = lambda x: quadratic_func(x, a[2], a[1], a[0])
    return func, a[2], a[1], a[0]


#полиномиальная функция 3-ей степени
def polynomial_approximation_3(x, y, cubic_func):
    n = len(x)
    SX = sum(x)
    SX2 = sum([p ** 2 for p in x])
    SX3 = sum([p ** 3 for p in x])
    SX4 = sum([p ** 4 for p in x])
    SX5 = sum([p ** 5 for p in x])
    SX6 = sum([p ** 6 for p in x])


    SY = sum(y)
    SXY = sum([x[i] * y[i] for i in range(n)])
    SX2Y = sum([x[i] * x[i] * y[i] for i in range(n)])
    SX3Y = sum([x[i] * x[i] * x[i] * y[i] for i in range(n)])

    x = np.array([[n, SX, SX2, SX3], [SX, SX2, SX3, SX4], [SX2, SX3, SX4, SX5], [SX3, SX4, SX5, SX6]])

    y = np.array([SY, SXY, SX2Y, SX3Y])
    a = np.linalg.solve(x, y)

    func = lambda x: cubic_func(x, a[3], a[2], a[1], a[0])
    return func, a[3], a[2], a[1], a[0]


#полиномиальная функция 4-ей степени
def polynomial_approximation_4(x, y, quadr):
    n = len(x)
    SX = sum(x)
    SX2 = sum([p ** 2 for p in x])
    SX3 = sum([p ** 3 for p in x])
    SX4 = sum([p ** 4 for p in x])
    SX5 = sum([p ** 5 for p in x])
    SX6 = sum([p ** 6 for p in x])
    SX7 = sum([p ** 7 for p in x])
    SX8 = sum([p ** 8 for p in x])


    SY = sum(y)
    SXY = sum([x[i] * y[i] for i in range(n)])
    SX2Y = sum([x[i] * x[i] * y[i] for i in range(n)])
    SX3Y = sum([x[i] * x[i] * x[i] * y[i] for i in range(n)])
    SX4Y = sum([x[i] * x[i] * x[i] * x[i] *y[i] for i in range(n)])

    x = np.array([[n, SX, SX2, SX3, SX4], [SX, SX2, SX3, SX4, SX5], [SX2, SX3, SX4, SX5, SX6], [SX3, SX4, SX5, SX6, SX7], [SX4, SX5, SX6, SX7, SX8]])
    y = np.array([SY, SXY, SX2Y, SX3Y, SX4Y])
    a = np.linalg.solve(x, y)

    func = lambda x: quadr(x, a[4], a[3], a[2], a[1], a[0])
    return func, a[4], a[3], a[2], a[1], a[0]


#экспоненциальная аппроксимация
def exponential_approximation(x, y, exponential_func):
    if all(p >= 0 for p in x) and all(p >= 0 for p in y):
        y_ln = [np.log(p) for p in y]
        _, b1, a1 = linear_approximation(x, y_ln, linear)
        b = np.exp(a1)
        a = b1
        func = lambda x: exponential_func(x, a, b)
        return func, a, b
    else:
        print("Использованы недопустимые значения для экспоненциальной функции")
        return None, None, None


#логарифмическая аппроксимация
def logarithmic_approximation(x, y, logarithmic_func):
    try:
        if not all([p > 0 for p in x]):
            return None, None, None
        x_ln = [np.log(p) for p in x]
        _, a1, b1 = linear_approximation(x_ln, y, linear)
        func = lambda x: logarithmic_func(x, a1, b1)
        return func, a1, b1
    except ValueError:
        print("Возникла ошибка при вычислениях")


#степенная аппроксимация
def power_approximation(x, y, power_func):
    if not (all([p > 0 for p in x]) and all([p > 0 for p in y])):
        return None, None, None
    x_ln = [np.log(p) for p in x]
    y_ln = [np.log(p) for p in y]
    _, b1, a1 = linear_approximation(x_ln, y_ln, linear)
    a = np.exp(a1)
    b = b1
    func = lambda x: power_func(x, a, b)
    return func, a, b


def get_S(f, x, y):
    try:
        return sum([(f(x[i]) - y[i]) ** 2 for i in range(len(x))])
    except TypeError:
        print("Данные некорректны")


def mean_squared_error(x, y, func):
    try:
        return np.sqrt(get_S(func, x, y) / len(x))
    except TypeError:
        print("Данные некорректны")


#позволяет определить наличие или отсутствие линейной связи между двумя переменными
def pearson_correlation_coefficient(x, y):
    x_ = sum([p for p in x]) / len(x)
    y_ = sum([p for p in y]) / len(y)
    return (sum([(x[i] - x_) * (y[i] - y_) for i in range(len(x))]) /
            np.sqrt(sum([(p - x_) ** 2 for p in x]) * sum([(p - y_) ** 2 for p in y])))


#чем ближе значение детерминации к единице, тем надежнее функция аппроксимирует исследуемый процесс
def coefficient_of_determination(x, y, func):
    phi = sum([p for p in x]) / len(x)
    return 1 - (sum([(y[i] - func(x[i])) ** 2 for i in range(len(x))]) / sum([(p - phi) ** 2 for p in y]))


def main():
    error_printed = {1: False, 2: False, 3: False, 4: False, 5: False, 6: False, 7: False}

    while True:
        choice = input("Выберите способ ввода данных f/c: ")
        if choice == "f":
            file_name = input("Введите имя файла: ")
            try:
                x, y = read_data_from_file(file_name)
                break
            except FileNotFoundError:
                print("Ошибка: Файл не найден.")
        elif choice == "c":
            x, y = input_data_from_console()
            break
        else:
            print("Ошибка: Введите 'f' или 'c'.")

    f1, a1, b1 = linear_approximation(x, y, linear)
    f2, a2, b2, c2 = polynomial_approximation_2(x, y, quadratic)
    f3, a3, b3, c3, d3 = polynomial_approximation_3(x, y, cubic)
    f4, a4, b4 = exponential_approximation(x, y, exponential)
    f5, a5, b5 = logarithmic_approximation(x, y, logarithmic)
    f6, a6, b6 = power_approximation(x, y, power)
    f7, a7, b7, c7, d7, e7 = polynomial_approximation_4(x, y, quadr)

    f = [f1, f2, f3, f4, f5, f6, f7]

    titles = ["Линейная аппроксимация", "Квадратичная аппроксимация", "Кубическая аппроксимация",
              "Экспоненциальная аппроксимация", "Логарифмическая аппроксимация", "Степенная аппроксимация", "Аппроксимация для полиномиальной функции 4-ей степени"]

    for i in range(7):
        try:
            if f[i] is None:
                print("Аппроксимация невозможна при введенных данных")
                continue

            if not error_printed[i+1]:
                print(titles[i])
                print("{:<3} {:<10} {:<10} {:<10} {:<10}".format("№", "X", "Y", "P", "E"))
                error_printed[i+1] = True

            for j in range(len(x)):
                print("{:<3} {:<10.3f} {:<10.3f} {:<10.3f} {:<10.3f}".format(j + 1, x[j], y[j], f[i](x[j]),
                                                                             f[i](x[j]) - y[j]))
            r2 = coefficient_of_determination(x, y, f[i])
            print(f"Коэффициент детерминации: {r2:.5f}")
            if r2 < 0.5:
                print("Точность аппроксимации недостаточна")
            elif r2 < 0.75:
                print("Слабая аппроксимация")
            elif r2 < 0.95:
                print("Удовлетворительная аппроксимация")
            else:
                print("Высокая точность аппроксимации")

            if i == 0:
                pr = pearson_correlation_coefficient(x, y)
                print(f"Коэффициент Пирсона: {pr:.5f}")
                if pr == 0:
                    print("Связь между переменными отсутствует")
                elif pr == 1 or pr == -1:
                    print("Строгая линейная зависимость")
                elif pr < 0.3:
                    print("Связь слабая")
                elif pr < 0.5:
                    print("Связь умеренная")
                elif pr < 0.7:
                    print("Связь заметная")
                elif pr < 0.9:
                    print("Связь высокая")
                else:
                    print("Связь весьма высокая")
        except TypeError:
            print("Данные некорректны")

    try:
        linear_mse = mean_squared_error(x, y, f1)
        polynomial_2_mse = mean_squared_error(x, y, f2)
        polynomial_3_mse = mean_squared_error(x, y, f3)
        exponential_mse = mean_squared_error(x, y, f4)
        if f5 is not None:
            logarithmic_mse = mean_squared_error(x, y, f5)
        else:
            logarithmic_mse = np.inf
        if f6 is not None:
            power_mse = mean_squared_error(x, y, f6)
        else:
            power_mse = np.inf

        fourth_mse = mean_squared_error(x, y, f7)


        approximations = ["Линейная", "Квадратичная", "Кубическая", "Экспоненциальная", "Логарифмическая", "Степенная", "Аппроксимация для полиномиальной функции 4-ей степени"]
        mses = [linear_mse, polynomial_2_mse, polynomial_3_mse, exponential_mse, logarithmic_mse, power_mse, fourth_mse]
        best_approximation_index = np.argmin(mses)
        print(f"Наилучшая аппроксимирующая функция: {approximations[best_approximation_index]}")

        plt.figure(figsize=(10, 6))
        plt.scatter(x, y, label='Исходные данные')
        x_ = np.linspace(min(x) - 1, max(x) + 1, 1000)
        for i in range(6):
            if f[i] is None:
                continue
            yi = np.array([f[i](a) for a in x_])
            plt.plot(x_, yi, label=titles[i])
        plt.legend()
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.grid()
        plt.show()
    except TypeError:
        print("Аппроксимация невозможна при введенных значениях")


if __name__ == '__main__':
    main()

