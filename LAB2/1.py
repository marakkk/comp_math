import numpy as np
import matplotlib.pyplot as plt


def method_half_division(a, b, epsilon, f):
    if f(a) * f(b) > 0:
        return None
    else:
        iter_count = 0
        c = (a + b) / 2
        print("{:^10} {:^10} {:^10} {:^10} {:^10} {:^10} {:^10} {:^10}".format("Iter", "a", "b", "x", "F(a)", "F(b)", "F(x)", "|a-b|"))

        while abs(b - a) >= epsilon or abs(f(c)) >= epsilon and abs(a-b) >= epsilon:
            if f(c) == 0:
                return c
            elif f(a) * f(c) < 0:
                b = c
            else:
                a = c
            c = (a + b) / 2

            iter_count += 1
            print("{:^10} {:.6f} {:.6f} {:.6f} {:.6f} {:.6f} {:.6f} {:.6f}".format(iter_count, a, b, c, f(a), f(b), f(c), abs(a-b)))

        return c, iter_count


def method_secant(a, b, epsilon, f):
    if f(a) * f(b) > 0:
        return None
    else:
        if diff(f, a) * diff2(f, a) > 0:
            x0 = a
            x1 = x0 + epsilon
        else:
            x0 = b
            x1 = a
        iter_count = 0

        if abs(f(x0)) < epsilon:
            return x0
        if abs(f(x1)) < epsilon:
            return x1
        print("{:^10} {:^10} {:^10} {:^10} {:^10} {:^10}".format("Iter", "x_i-1", "x_i", "x_i+1", "f(x_i+1)", "|x_i+1 - x_i|"))

        while True:
            x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
            if np.abs(x2 - x1) < epsilon:
                return x2, iter_count
            x0 = x1
            x1 = x2
            iter_count += 1
            print("{:^10} {:.6f} {:.6f} {:.6f} {:.6f} {:.6f}".format(iter_count, x0, x1, x2, f(x2), abs(x2 - x1)))


def phi(fn, la, x):
    return x + la * fn

def phi_sh(fn, la):
    return 1 + la*fn

def diff(f, x, h=1e-6):
    return (f(x + h) - f(x)) / h


def diff2(f, x0):
    h = 1e-6
    return (f(x0 + h) - 2 * f(x0) + f(x0 - h)) / (pow(h, 2))


def diff_fi(la, x, f):
    h = 1e-6
    return (x + h + la * f(x + h) - x - la * f(x)) / h


def method_simple_iteration(a, b, eps, func):
    if diff(func, a) * diff2(func, a) > 0:
        x = a
    else:
        x = b
    iter_count = 0
    if diff(func, a) > 0 or diff(func, b) > 0:
        lambd = -1
    else:
        lambd = 1
    lambd *= 1 / max(abs(diff(func, a)), abs(diff(func, b)))

    fl = True
    print("{:^10} {:^10} {:^10} {:^10} {:^10} {:^10}".format("Iter", "x_i", "x_i+1", "phi(x_i+1)", "f(x_i+1)", "|x_i+1 - x_i|"))

    while True:
        if ((diff_fi(lambd, a, func)) > 1 or abs(diff_fi(lambd, b, func)) > 1) and fl:
            print("Расходится. Значение функции в точке x = {:.6f}: {:.6f}".format(diff_fi(lambd, a, func), diff_fi(lambd, b, func)))
            fl = False

        x_new = phi(func(x), lambd, x)
        iter_count += 1
        print("{:^10} {:.6f} {:.6f} {:.6f} {:.6f} {:.6f}".format(iter_count, x, x_new, phi(func(x_new), lambd, x_new),
                                                                 func(x_new), abs(x_new - x)))
        x = x_new

        if abs(x_new - x) <= eps and abs(func(x_new)) <= eps:
            return x, iter_count


def verify_input_data(a, b, f):
    if f(a) * f(b) > 0:
        return False
    else:
        return True


def plot_function(f):
    a = -4
    b = 4
    x = np.linspace(a - 1, b + 1, 100)
    y = f(x)
    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('График функции')
    plt.grid(True)

    plt.show()


def plot_function_root(f, a, b, root):
    x = np.linspace(a - 1, b + 1, 100)
    y = f(x)
    plt.plot(x, y, label='f(x)')
    plt.plot(root, f(root), 'ro', label='Root')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('График функции с найденным корнем')
    plt.legend()
    plt.grid(True)
    plt.show()


def read_input_data_from_file():
    with open('input', 'r') as file:
        a, b, epsilon = map(float, file.readline().split())
    return a, b, epsilon


def read_input_data_from_keyboard():
    a = float(input("Введите левую границу интервала: "))
    b = float(input("Ввведите правую границу интервала: "))
    epsilon = float(input("Введите погрешность: "))
    return a, b, epsilon


def write_result_to_file(root, f, iter_count):
    with open('out', 'w') as file:
        file.write("Найденный корень уравнения: {}\n".format(root))
        file.write("Значение функции в корне: {}\n".format(f(root)))
        file.write("Количество итераций: {}\n".format(iter_count))


def write_result_to_screen(root, f, iter_count):
    print("Найденный корень уравнения: {}".format(root))
    print("Значение функции в корне: {}".format(f(root)))
    print("Количество итераций: {}".format(iter_count))


def select_equation():
    print("Выберите уравнение:")
    print("1. x^3 - x + 4")
    print("2. e^x - 6x - 3")
    print("3. x^3 + 2.84x^2 - 5.606x - 14.766")
    print("4. 4.45x^3 + 7.81x^2 - 9.62x - 8.17")
    choice = int(input("Введите номер выбранного уравнения: "))
    if choice == 1:
        return lambda x: x ** 3 - x + 4
    elif choice == 2:
        return lambda x: np.exp(x) - 6 * x - 3
    elif choice == 3:
        return lambda x: x ** 3 + 2.84 * x ** 2 - 5.606 * x - 14.766
    elif choice == 4:
        return lambda x: 4.45 * x ** 3 + 7.81 * x ** 2 - 9.62 * x - 8.17

    else:
        print("Неверный ввод")
        return None


def select_method():
    print("Выберите метод решения:")
    print("1. Метод половинного деления")
    print("2. Метод секущих")
    print("3. Метод простых итераций")
    choice = int(input("Введите номер выбранного метода: "))
    return choice


def main():
    f = select_equation()
    plot_function(f)

    choice = input("Ввод исходных данных файл или консоль (f/s): ")
    if choice == 'f':
        a, b, epsilon = read_input_data_from_file()

    elif choice == 's':
        a, b, epsilon = read_input_data_from_keyboard()

    else:
        print("Неверный ввод")
        return

    if epsilon <= 0:
        print("Погрешность должна быть положительным числом")
        return

    roots_count = verify_input_data(a, b, f)
    if roots_count == 0:
        print("Корней на данном отрезке не существует")
        return
    elif roots_count > 1:
        print("На данном отрезке несколько корней")
        return

    method = select_method()

    if method == 1:
        root, iter_count = method_half_division(a, b, epsilon, f)
    elif method == 2:
        root, iter_count = method_secant(a, b, epsilon, f)
    elif method == 3:

        root, iter_count = method_simple_iteration(a, b, epsilon, f)
    else:
        print("Неверный ввод")
        return

    if root is not None:
        choice = input("Вывести результат работы программы в файл или консоль (f/s): ")
        if choice == 'f':
            write_result_to_file(root, f, iter_count)
        elif choice == 's':
            write_result_to_screen(root, f, iter_count)

    plot_function_root(f, a, b, root)


if __name__ == '__main__':
    main()
