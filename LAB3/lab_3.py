import math
import scipy.integrate as sci

# Функции для вычисления значений функции
def function_1(x):
    return x ** 2


def function_2(x):
    return 2 * x ** 3 - 3 * x ** 2 + 5 * x - 9


def function_3(x):
    return -x ** 3 - x ** 2 + x + 3


def function_4(x):
    return 2 * x ** 3 - 9 * x ** 2 - 7 * x + 11


def function_5(x):
    return 1 / x**2

# Функции для вывода уравнений функций
def print_functions():
    print("1. x^2")
    print("2. 2x^3 - 3x^2 + 5x - 9")
    print("3. -x^3 - x^2 + x + 3")
    print("4. 2x^3 - 9x^2 - 7x + 11")


# Методы численного интегрирования
def left_rectangle_method(func, a, b, n):
    h = (b - a) / n
    res = 0
    for i in range(n):
        res += h * func(a + i * h)
    return res


def right_rectangle_method(func, a, b, n):
    h = (b - a) / n
    res = 0
    for i in range(1, n + 1):
        res += h * func(a + i * h)
    return res


def middle_rectangle_method(func, a, b, n):
    h = (b - a) / n
    res = 0
    for i in range(n):
        res += h * func(a + (i + 0.5) * h)

    return res


def trapezoidal_method(func, a, b, n):
    h = (b - a) / n
    res = 0
    for i in range(1, n + 1):
        res += 0.5 * h * (func(a + (i - 1) * h) + func(a + i * h))
    return res


def simpsons_method(func, a, b, n):
    h = (b - a) / n
    res = func(a) + func(b)
    for i in range(1, n):
        x = a + i * h
        if i % 2 == 0:
            res += 2 * func(x)
        else:
            res += 4 * func(x)
    res *= h / 3
    return res


# Правило Рунге для оценки погрешности
def runge_rule(f, a, b, n, method, e):
    if method == simpsons_method:
        k = 4
    elif method == left_rectangle_method or method == right_rectangle_method:
        k = 1
    else:
        k = 2
    try:
        I0 = method(f, a, b, n)
        print('n =', n, 'Значение интеграла =', I0)

        I1 = method(f, a, b, n * 2)
        n *= 2
        print('n = ', n, 'Значение интеграла = ', I1)

        while abs((I1 - I0) / (2 ** k - 1)) > e:
            I0 = I1
            n *= 2

            I1 = method(f, a, b, n)
            print('n = ', n, 'Значение интеграла = ', I1)

        lib_int, _ = sci.quad(f, a, b)
        print(f'Значение интеграла (библиотека): {lib_int}')
        return n, I1
    except TypeError:
        print("Интеграл не существует")



# Функция для проверки сходимости и наличия бесконечных разрывов
def check_convergence(func, a, b):
    try:
        for point in [a, b, (a+b)/2]:
            func_value = func(point)
            if math.isinf(func_value) or math.isnan(func_value):
                print("Интеграл не существует из-за бесконечного разрыва.")
                return False
        return True
    except Exception as e:
        print("Ошибка при проверке сходимости:", e)
        return False


# Ввод пользовательских данных
def get_user_input():
    print_functions()
    function_choice = int(input("Выберите функцию для интегрирования: "))
    a = float(input("Введите нижний предел интегрирования: "))
    b = float(input("Введите верхний предел интегрирования: "))
    n = 4  # начальное значение числа разбиения
    accuracy = float(input("Введите требуемую точность: "))
    return function_choice, a, b, n, accuracy


# Основная функция вычисления интеграла с заданной точностью
def compute_integral():
    function_choice, a, b, n, accuracy = get_user_input()
    if function_choice == 1:
        func = function_1
        print("Выбрано уравнение: 1")
    elif function_choice == 2:
        func = function_2
        print("Выбрано уравнение: 2")
    elif function_choice == 3:
        func = function_3
        print("Выбрано уравнение: 3")
    elif function_choice == 4:
        func = function_4
        print("Выбрано уравнение: 4")
    elif function_choice == 5:
        func = function_5
    else:
        raise ValueError("Некорректный выбор")


    print("Выберите метод интегрирования:")
    print("1. Метод прямоугольников (левые)")
    print("2. Метод прямоугольников (правые)")
    print("3. Метод прямоугольников (средние)")
    print("4. Метод трапеций")
    print("5. Метод Симпсона")
    print("6. Все методы выше разом")
    method_choice = int(input("Ваш выбор: "))


    if method_choice == 1:
        runge_rule(func, a, b, n, left_rectangle_method, accuracy)

    elif method_choice == 2:
        runge_rule(func, a, b, n, right_rectangle_method, accuracy)


    elif method_choice == 3:
        runge_rule(func, a, b, n, middle_rectangle_method, accuracy)

    elif method_choice == 4:
        runge_rule(func, a, b, n, trapezoidal_method, accuracy)

    elif method_choice == 5:
        runge_rule(func, a, b, n, simpsons_method, accuracy)

    elif method_choice == 6:
        print("Метод левых прямоугольников:")
        runge_rule(func, a, b, n, left_rectangle_method, accuracy)

        print("Метод правых прямоугольников:")
        runge_rule(func, a, b, n, right_rectangle_method, accuracy)

        print("Метод средних прямоугольников:")
        runge_rule(func, a, b, n, middle_rectangle_method, accuracy)

        print("Метод трапеций:")
        runge_rule(func, a, b, n, trapezoidal_method, accuracy)

        print("Метод Симпсона:")
        runge_rule(func, a, b, n, simpsons_method, accuracy)


    else:
        raise ValueError("Некорректный выбор метода")


# Вызов основной функции
compute_integral()
