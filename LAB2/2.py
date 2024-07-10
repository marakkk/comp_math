import numpy as np
import matplotlib.pyplot as plt

def f1_x1(x, y):
    return x - np.cos(y) - 3


def f1_x2(x, y):
    return np.cos(x - 1) - 0.5 + y

def phi1_x1(x, y):
    return np.cos(y) + 3


def phi1_x2(x, y):
    return -np.cos(x - 1) + 0.5


def phi3_x1(x, y):
    return 0.3 - 0.1*x**2 - 0.2*y**2


def phi3_x2(x, y):
    return 0.7 - 0.2*x**2 - 0.1*x*y


def df3_dx(x, y):
    return -0.2 * x


def df3_dy(x, y):
    return -0.4 * y


def df1_dx(x, y):
    return 0


def df1_dy(x, y):
    return -np.sin(y)


def dg1_dx(x, y):
    return np.sin(x-1)


def dg1_dy(x, y):
    return 0


def dg3_dx(x, y):
    return -0.4 * x - 0.1 * y


def dg3_dy(x, y):
    return -0.1 * x


# Функция метода простой итерации
def simple_iteration_method(phi1, phi2, x0, y0, epsilon):
    x_prev, y_prev = x0, y0
    iterations = 0
    x_errors = []
    y_errors = []
    max_it = 50

    while True:
        x_next = phi1(x_prev, y_prev)
        y_next = phi2(x_prev, y_prev)

        x_error = abs(x_next - x_prev)
        y_error = abs(y_next - y_prev)

        x_errors.append(x_error)
        y_errors.append(y_error)

        if max(x_error, y_error) <= epsilon or iterations > max_it:
            return x_next, y_next, iterations, x_error, y_error

        x_prev, y_prev = x_next, y_next
        iterations += 1
        print(iterations)
        print(x_next)
        print(y_next)


def choose_system():
    print("Выберите систему уравнений:")
    print("1. \n    cos(x - 1) + y = 0.5\n    x - cos(y) = 3 ")
    print("2. \n    0.1x^2 + x + 0.2y^2 - 0.3 = 0\n    0.2x^2 + y + 0.1xy - 0.7 = 0 ")

    choice = int(input("Введите номер выбранного уравнения: "))
    if choice == 1:
        return phi1_x1, phi1_x2, df1_dx, df1_dy, dg1_dx, dg1_dy , 1

    elif choice == 2:
        return phi3_x1, phi3_x2, df3_dx, df3_dy, dg3_dx, dg3_dy,2
    else:
        print("Некорректный ввод. Пожалуйста, выберите 1 или 2.")
        return choose_system()


# Функция для вывода результатов
def print_results(solution, iterations, x_errors, y_errors):
    print(f"Результаты для системы уравнений: \n")
    print(f"Решение: x = {solution[0]}, y = {solution[1]}")
    print(f"Количество итераций: {iterations}")
    print("Вектор погрешностей по x на каждой итерации:")
    print(x_errors)
    print("Вектор погрешностей по y на каждой итерации:")
    print(y_errors)


def plot_equations_with_intersection(func_num):

    x = np.linspace(-10, 10, 400)
    y = np.linspace(-10, 10, 400)
    X, Y = np.meshgrid(x, y)

    if func_num ==1:

        Z1 = np.cos(X + 1) +Y -0.5
        Z2 = X - np.cos(Y) - 3
    else:
        Z1 = 0.1 * X**2 + X +0.2*Y**2 - 0.3
        Z2 = 0.2 * X**2 + Y +0.2*Y*X - 0.7
    plt.figure()
    contours1 = plt.contour(X, Y, Z1, levels=[0], colors='blue')

    contours2 = plt.contour(X, Y, Z2, levels=[0], colors='red')

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('График системы уравнений')
    plt.grid(True)
    plt.show()


def read_input_data():
    x0 = float(input("Введите начальное приближение x: "))
    y0 = float(input("Ввведите начальное приближение y: "))
    epsilon = float(input("Введите погрешность: "))
    return x0, y0, epsilon

def main():
    phi1, phi2, df_dx, df_dy, dg_dx, dg_dy, n = choose_system()
    print(f"Решение для выбранной системы уравнений:")
    x0, y0, eps = read_input_data()

    # Проверка достаточного условия сходимости
    if max(abs(df_dx(x0, y0)) + abs(df_dy(x0, y0)), abs(dg_dx(x0, y0)) + abs(dg_dy(x0, y0))) < 1:
        print("Достаточное условие сходимости выполнено.")
    else:
        print("Достаточное условие сходимости не выполнено.")


    # Выполнение метода простой итерации
    x_next, y_next, iterations, x_errors, y_errors = simple_iteration_method(phi1, phi2, x0, y0, eps)

    # Вывод результатов
    print_results((x_next, y_next), iterations, x_errors, y_errors)

    # Построение графика функций
    plot_equations_with_intersection(n)


if __name__ == '__main__':
    main()


#выводить значение функции
