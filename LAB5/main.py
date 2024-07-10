import numpy as np
import math
from extra_task import bessel_interpolation, stirling_interpolation
from input_console import get_input_method, input_from_keyboard, input_from_file, select_function
from main_task import interpolate_newton_forward_diff, interpolate_newton_backward_diff, interpolate_newton_divided_diff, interpolate_lagrange
from plot_and_tables import print_difference_table, print_divided_difference_table, plot_interpolation


def are_nodes_equally_spaced(x):
    return all(math.isclose(x[i + 1] - x[i], x[1] - x[0]) for i in range(len(x) - 1))


def main():
    method = get_input_method()
    if method == 1:
        x, y = input_from_keyboard()
    elif method == 2:
        x, y = input_from_file()
    elif method == 3:
        x, y = select_function()

    equally_spaced = are_nodes_equally_spaced(x)

    x_interp = float(input("Введите значение аргумента для интерполяции: "))

    n = len(x)
    mid_index = n // 2

    if equally_spaced:
        h = x[1] - x[0]
        if x_interp <= x[mid_index]:
            t = (x_interp - x[0]) / h
            print(t)

            y_interp_newton = interpolate_newton_forward_diff(x, y, x_interp)
            method_name = "Ньютона (вперед)"
        else:
            t = (x_interp - x[-1]) / h
            y_interp_newton = interpolate_newton_backward_diff(x, y, x_interp)
            print(t)

            method_name = "Ньютона (назад)"

        print_difference_table(x, y)

    else:
        y_interp_newton = interpolate_newton_divided_diff(x, y, x_interp)
        print("Узлы являются неравноотстоящими")
        method_name = "Ньютона (разделенные разности)"

    y_interp_lagrange = interpolate_lagrange(x, y, np.array(x_interp).reshape(1, ))[0]
    y_interp_bessel = None
    y_interp_stirling = None

    h = x[1] - x[0]
    t = (x_interp - x[0]) / h

    if 0.25 <= abs(t) <= 0.75:
        if len(x) % 2 == 0:
            y_interp_bessel = bessel_interpolation(x, y, x_interp)
        else:
            print("Для интерполяции Бесселя необходимо четное количество узлов.")
    elif abs(t) <= 0.25:
        if len(x) % 2 != 0:
            y_interp_stirling = stirling_interpolation(x, y, x_interp)
        else:
            print("Для интерполяции Стирлинга необходимо нечетное количество узлов.")

    print(f"Приближенное значение функции в точке {x_interp} по методу {method_name}: {y_interp_newton}")
    print(f"Приближенное значение функции в точке {x_interp} по методу Лагранжа: {y_interp_lagrange}")

    if y_interp_bessel is not None:
        print(f"Приближенное значение функции в точке {x_interp} по методу Бесселя: {y_interp_bessel}")
    if y_interp_stirling is not None:
        print(f"Приближенное значение функции в точке {x_interp} по методу Стирлинга: {y_interp_stirling}")

    interp_x = np.linspace(min(x), max(x), 500)
    if equally_spaced:
        if t >= 0:
            interp_y_newton = [interpolate_newton_forward_diff(x, y, xi) for xi in interp_x]
        else:
            interp_y_newton = [interpolate_newton_backward_diff(x, y, xi) for xi in interp_x]
    else:
        interp_y_newton = [interpolate_newton_divided_diff(x, y, xi) for xi in interp_x]
    interp_y_lagrange = [interpolate_lagrange(x, y, xi) for xi in interp_x]

    plot_interpolation(x, y, interp_x, interp_y_newton, interp_y_lagrange, "")


if __name__ == "__main__":
    main()

