import matplotlib.pyplot as plt
from main_task import finite_differences, finite_forward_differences


def plot_interpolation(x, y, x_interp, y_interp_newton, y_interp_lagrange, func_name):
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, 'bo', label='Узлы интерполяции')

    if y_interp_newton is not None:
        plt.plot(x_interp, y_interp_newton, 'r-', label='Интерполяционный многочлен Ньютона')
    plt.plot(x_interp, y_interp_lagrange, 'g-', label='Интерполяционный многочлен Лагранжа')

    plt.legend()
    plt.title(f'Интерполяция функции {func_name}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.show()


def print_difference_table(x, y):
    n = len(x)
    forward_diff = finite_forward_differences(y)

    print("Таблица конечных разностей:")
    header = "№\txi\t\t\tyi"
    for j in range(1, n):
        header += f"\t\tΔ{j}yi"
    print(header)

    for i in range(n):
        row = f"{i}\t{x[i]:.2f}\t\t{y[i]:.2f}"
        for j in range(1, n - i):
            row += f"\t\t{forward_diff[i][j]:.2f}"
        print(row)
    print("\n")


def divided_differences(x, y):
    n = len(x)
    diff_table = [[0 for _ in range(n)] for _ in range(n)]

    # Fill the first column with y values
    for i in range(n):
        diff_table[i][0] = y[i]

    # Calculate divided differences
    for j in range(1, n):
        for i in range(n - j):
            diff_table[i][j] = (diff_table[i + 1][j - 1] - diff_table[i][j - 1]) / (x[i + j] - x[i])

    return diff_table


def print_divided_difference_table(x, y):
    n = len(x)
    diff_table = divided_differences(x, y)

    print("Таблица разделенных разностей:")
    header = "№\txi\t\t\tyi"
    for j in range(1, n):
        header += f"\t\tΔ{j}yi"
    print(header)

    for i in range(n):
        row = f"{i}\t{x[i]:.2f}\t\t{diff_table[i][0]:.2f}"
        for j in range(1, n - i):
            row += f"\t\t{diff_table[i][j]:.2f}"
        print(row)
    print("\n")
