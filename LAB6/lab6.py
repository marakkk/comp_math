import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate


def f1(x, y):
    return x ** 3


def f2(x, y):
    return 2 * x


def f3(x, y):
    return x ** 2


def select_equation():
    while True:
        print("Выберите уравнение:")
        print("1. y' = x^3")
        print("2. y' = 2x")
        print("3. y' = x^2")

        try:
            choice = int(input("Введите номер уравнения: "))
            equations = {1: f1, 2: f2, 3: f3}
            return equations[choice]
        except KeyError:
            print("Ошибка: Неверный ввод. Пожалуйста, введите номер уравнения из списка.")
        except ValueError:
            print("Ошибка: Введите целое число.")


def exact_solution(x, equation, y0):
    if equation == f1:
        C = y0 - (x[0] ** 4 / 4)
        return (x ** 4 / 4) + C
    elif equation == f2:
        C = y0 - x[0] ** 2
        return x ** 2 + C
    elif equation == f3:
        C = y0 - (x[0] ** 3 / 3)
        return x ** 3 / 3 + C


def modified_euler(f, y0, x0, xn, h):
    x_points = np.arange(x0, xn + h, h)
    y_points = [y0]

    for i in range(1, len(x_points)):
        x_current = x_points[i-1]
        y_current = y_points[-1]

        if x_current + h > xn:
            h = xn - x_current

        y_predictor = y_current + h * f(x_current, y_current)
        y_corrector = y_current + h/2 * (f(x_current, y_current) + f(x_current + h, y_predictor))

        y_points.append(y_corrector)

    return x_points, y_points


def runge_kutt(f, y0, a, b, h):
    n = int((b - a) / h)
    x = np.linspace(a, b, n + 1)
    y = np.zeros(n + 1)
    y[0] = y0
    for i in range(n):
        k1 = h * f(x[i], y[i])
        k2 = h * f(x[i] + h / 2, y[i] + k1 / 2)
        k3 = h * f(x[i] + h / 2, y[i] + k2 / 2)
        k4 = h * f(x[i] + h, y[i] + k3)
        y[i + 1] = y[i] + (k1 + 2 * k2 + 2 * k3 + k4) / 6
    return x, y


def adams(f, y0, a, b, h, epsilon):
    x = np.arange(a, b + h, h)
    y = np.zeros(len(x))
    y[0] = y0

    for i in range(1, 4):
        k1 = h * f(x[i - 1], y[i - 1])
        k2 = h * f(x[i - 1] + 0.5 * h, y[i - 1] + 0.5 * k1)
        k3 = h * f(x[i - 1] + 0.5 * h, y[i - 1] + 0.5 * k2)
        k4 = h * f(x[i], y[i - 1] + k3)
        y[i] = y[i - 1] + (k1 + 2 * k2 + 2 * k3 + k4) / 6

    for i in range(3, len(x) - 1):
        y_pred = y[i] + h * (55 * f(x[i], y[i]) - 59 * f(x[i - 1], y[i - 1]) + 37 * f(x[i - 2], y[i - 2]) - 9 * f(x[i - 3], y[i - 3])) / 24

        while True:
            y_corr = y[i] + h * (9 * f(x[i + 1], y_pred) + 19 * f(x[i], y[i]) - 5 * f(x[i - 1], y[i - 1]) + f(x[i - 2], y[i - 2])) / 24

            if np.abs(y_corr - y_pred) < epsilon:
                y[i + 1] = y_corr
                break
            else:
                y_pred = y_corr

    return x, y


def check_euler(f, y0, x0, xn, h1, h2, p):
    _, y_h1 = modified_euler(f, y0, x0, xn, h1)
    _, y_h2 = modified_euler(f, y0, x0, xn, h2)

    return np.abs(y_h1[-1] - y_h2[-1]) / (2 ** p - 1)


def check_runge(f, y0, x0, xn, h1, h2, p):
    _, y_h1 = runge_kutt(f, y0, x0, xn, h1)
    _, y_h2 = runge_kutt(f, y0, x0, xn, h2)

    return np.abs(y_h1[-1] - y_h2[-1]) / (2 ** p - 1)


def plot_results(t, y_modified_euler, y_rk4, y_adams, exact_y):
    plt.plot(t, y_modified_euler, label='Модифицированный метод Эйлера')
    plt.plot(t, y_rk4, label='Метод Рунге-Кутта 4-го порядка')
    plt.plot(t, y_adams, label='Метод Адамса')
    if exact_y is not None:
        plt.plot(t, exact_y, label='Точное решение')

    plt.legend()
    plt.xlabel('t')
    plt.ylabel('y(t)')
    plt.title('Численное решение ОДУ')
    plt.grid(True)
    plt.show()


def print_table(x_points, y_euler, y_rk4, y_adams, exact_y):
    table_dict = {}
    for i in range(len(x_points)):
        row = [
            i,
            x_points[i],
            y_euler[i],
            y_rk4[i],
            y_adams[i],
            exact_y[i]
        ]
        table_dict[i] = row

    headers = ["i", "x_i", "Мод. Эйлер", "Рунге-Кутта", "Адамс", "Точные значения"]

    print(tabulate(table_dict.values(), headers=headers, tablefmt="grid"))


def main():
    equation = select_equation()
    while True:
        try:
            y0 = float(input("Введите начальное значение y0: "))
            break
        except ValueError:
            print("Ошибка: Введите число для начального значения y0.")

    while True:
        try:
            a = float(input("Введите начальное значение: "))
            break
        except ValueError:
            print("Ошибка: Введите число для начального значения a.")

    while True:
        try:
            b = float(input("Введите конечное значение: "))
            if b <= a:
                print("Ошибка: Конечное значение должно быть больше начального значения .")
            else:
                break
        except ValueError:
            print("Ошибка: Введите число для конечного значения.")

    while True:
        try:
            h = float(input("Введите шаг интегрирования: "))
            if h <= 0:
                print("Ошибка: Шаг интегрирования должен быть положительным числом.")
            else:
                break
        except ValueError:
            print("Ошибка: Введите число для шага интегрирования.")

    while True:
        try:
            eps = float(input("Введите погрешность: "))
            if eps <= 0:
                print("Ошибка: Погрешность должна быть положительным числом.")
            elif eps > 0.1:
                print("Ошибка. Введенная погрешность слишком велика.")
            else:
                break
        except ValueError:
            print("Ошибка: Введите число для погрешности.")

    x_points = np.arange(a, b + h, h)

    t_euler, y_euler = modified_euler(equation, y0, a, b, h)

    t_rk4, y_rk4 = runge_kutt(equation, y0, a, b, h)

    t_adams, y_adams = adams(equation, y0, a, b, h / 2, eps)

    exact_x = np.linspace(a, b, len(x_points))
    exact_y = exact_solution(exact_x, equation, y0)

    y_euler_interp = np.interp(x_points, t_euler, y_euler)
    y_rk4_interp = np.interp(x_points, t_rk4, y_rk4)
    y_adams_interp = np.interp(x_points, t_adams, y_adams)

    print_table(x_points, y_euler_interp, y_rk4_interp, y_adams_interp, exact_y)

    epsilon = check_euler(equation, y0, a, b, h, h / 2, 1)

    while epsilon > eps:
        h = h / 2
        _, y_euler_half = modified_euler(equation, y0, a, b, h / 2)
        epsilon = check_euler(equation, y0, a, b, h, h / 2, 2)

    print(f"Точность метода модифицированного Эйлера по правилу Рунге: {epsilon}")

    epsilon = check_runge(equation, y0, a, b, h, h / 2, 4)

    while epsilon > eps:
        h = h / 2
        epsilon = check_runge(equation, y0, a, b, h, h / 2, 4)

    print(f"Точность метода Рунге-Кутта по правилу Рунге: {epsilon}")

    plot_results(x_points, y_euler_interp, y_rk4_interp, y_adams_interp, exact_y)


if __name__ == "__main__":
    main()
