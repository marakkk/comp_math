import sys
import numpy as np

print("<-- Решение СЛАУ методом Гаусса с выбором главного элемента по столбцам -->\n")

def print_matrix_iteration(matrix, vector, iteration):
    print(f"Матрица на итерации {iteration}:")
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if j == iteration:
                print("0", end=" ")
            else:
                print(matrix[i][j], end=" ")
        print("|", vector[i])



def gauss_method_main_el(matrix, vector):
    n = len(matrix)
    det = 1

    print("Исходная матрица:")
    for t in range(n):
        print(matrix[t], vector[t], sep="|")
    print()

    # Проходим по каждой строке матрицы
    for i in range(n):
        max_el = abs(matrix[i][i])  # Инициализируем максимальный элемент текущей строки
        max_row = i  # Инициализируем индекс строки

        print(f"Итерация {i + 1}:")

        # Находим строку с максимальным элементом в текущем столбце
        for k in range(i + 1, n):
            if abs(matrix[k][i]) > max_el:
                max_el = abs(matrix[k][i])
                max_row = k

        print(f"Максимальный элемент в столбце {i + 1} найден в строке {max_row + 1}: {max_el}")

        # Если индекс строки с максимальным элементом не совпадает с текущей строкой, меняем строки местами
        if i != max_row:
            matrix[i], matrix[max_row] = matrix[max_row], matrix[i]
            vector[i], vector[max_row] = vector[max_row], vector[i]
            det *= -1

            print(f"Меняем строки местами: строка {i + 1} и строка {max_row + 1}")
            print("Новая матрица после выбора главного элемента:")
            for t in range(n):
                print(matrix[t], vector[t], sep="|")
            print()
        else:
             print("Новая матрица после выбора главного элемента:")
             for t in range(n):
                print(matrix[t], vector[t], sep="|")

             print()




        det *= matrix[i][i]  # Считаем определитель с учетом элемента на диагонали
        if det == 0:
            print("Матрица не может быть решена методом Гаусса, так как определитель матрицы равен нулю")
            sys.exit()

        # Прямой ход метода Гаусса


        for k in range(i + 1, n):                                                                                                         
            if matrix[i][i] == 0:                                                                                                         
                print("Диагональный элемент равен нулю. Решения могут быть бесконечными или отсутствовать.")                              
                sys.exit()                                                                                                                
            c = -matrix[k][i] / matrix[i][i]                                                                                              
                                                                                                                                      
            #print(f"Вычитаем из строки {k + 1} строку {i + 1} умноженную на коэффициент {c}:")                                           
            for j in range(i, n):                                                                                                         
                if i == j:                                                                                                                
                    matrix[k][j] = 0                                                                                                      
                else:                                                                                                                     
                    matrix[k][j] += c * matrix[i][j]                                                                                      
            vector[k] += c * vector[i]                                                                                                    

            for t in range(n):
               print(matrix[t], vector[t], sep="|")
            print()




    try:
        print("Матрица в треугольном виде:")
        for t in range(n):
            print(matrix[t], vector[t], sep="|")
    except IndexError:
        print("Матрица не корректна, невозможно выполнить метод Гаусса")

    # Проводим обратный ход метода Гаусса для нахождения решения системы
    try:
        x = [0 for i in range(n)]
        for i in range(n - 1, -1, -1):
            if matrix[i][i] == 0:
                print("Диагональный элемент равен нулю. Решения могут быть бесконечными или отсутствовать.")
                sys.exit()
            x[i] = vector[i] / matrix[i][i]
            for k in range(i - 1, -1, -1):
                vector[k] -= matrix[k][i] * x[i]

    except ZeroDivisionError:
        x = 0
        print("Матрица не корректна, решений нет")

    print("\nОпределитель матрицы:", det)
    return x


def ordinary_gauss_method(matrix, b):
    n = len(matrix)

    # Прямой ход
    for i in range(n):
        # Поиск строки с максимальным элементом в текущем столбце
        max_index = i
        for j in range(i + 1, n):
            if abs(matrix[j][i]) > abs(matrix[max_index][i]):
                max_index = j
        # Обмен строк для улучшения численной устойчивости
        if max_index != i:
            matrix[i], matrix[max_index] = matrix[max_index], matrix[i]
            b[i], b[max_index] = b[max_index], b[i]
        # Проход по всем строкам ниже текущей
        for j in range(i + 1, n):
            coeff = matrix[j][i] / matrix[i][i]
            for k in range(i, n):
                matrix[j][k] -= coeff * matrix[i][k]
            b[j] -= coeff * b[i]


    # Обратный ход
    x = [0] * n
    for i in range(n - 1, -1, -1):
        x[i] = b[i] / matrix[i][i]
        for j in range(i + 1, n):
            x[i] -= matrix[i][j] * x[j] / matrix[i][i]

    return x


def find_residual(matrix, vector, solution):
    try:
        n = len(matrix)
        residuals = []
        for i in range(n):
            summary = 0
            for j in range(n):
                summary += matrix[i][j] * solution[j]
            residuals.append(vector[i] - summary)

        print("\nВектор невязки:", residuals)
        return residuals

    except IndexError:
        print("Вектор невязки невозможно посчитать, так как была допущена ошибка")


class OutOfRangeException(Exception):
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return repr(self.data)


class BlankSpaceException(Exception):
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return repr(self.data)


def check_input_console():
    press = input("Введите '1' для работы через консоль, или введите '2' для работы с файлом: \n")
    while press != '':
        if int(press) == 1:

            try:
                n = int(input("Введите размерность матрицы: \n"))

                if n == 0 or n == 1 or n >= 20 or n < 0:
                    raise OutOfRangeException("Матрица этой размерности не валидна")

                matrix = []
                print("Введите матрицу построчно через пробел:")

                for i in range(n):
                    row = input().split()
                    if len(row) != n:
                        print("Неправильное количество элементов в строке. Пожалуйста, введите строку заново.")
                        sys.exit()
                    matrix.append([float(j) for j in row])

                vector = []
                print("Введите вектор b построчно:")
                for i in range(n):
                    vector.append(float(input()))

                result = gauss_method_main_el(matrix, vector)

                solution = ordinary_gauss_method(matrix, vector)
                find_residual(matrix, vector, solution)

                if result == 0:
                    print("Решений для данной матрицы не существует")
                else:
                    print("\nПолученные неизвестные векторы:", result)

                numpy_solution = np.linalg.solve(matrix, vector)
                if np.allclose(solution, numpy_solution):
                    print("Решение, полученное с использованием сторонней библиотеки, совпадает с решением методом "
                          "Гаусса.")
                    print(numpy_solution)
                else:
                    print("Решения, полученное с использованием сторонней библиотеки, не совпадают.")

                break
            except ValueError:
                print("Введенные данные некорректны, попробуйте снова")
            except OutOfRangeException as e:
                print("Вызвана ошибка: ", e.data)
            except IndexError:
                print("Введенные данные не корректны")

        elif int(press) == 2:
            filename = input("Введите имя файла для чтения: \n")
            matrix = []
            vector = []
            try:
                with open(filename, "r+") as file:
                    for line in file:
                        try:
                            numbers = list(map(float, line.split()))
                            if len(numbers) > 2:
                                matrix.append(numbers[:-1])
                                vector.append(numbers[-1])
                        except ValueError:
                            print("Ошибка: Невозможно преобразовать строку в число")
                            continue

                if not matrix or not vector:
                    print("Данные в файле некорректны")
                    sys.exit()

                print(matrix)
                numpy_solution = np.linalg.solve(matrix, vector)
                print(numpy_solution)

                result = gauss_method_main_el(matrix, vector)

                solution = ordinary_gauss_method(matrix, vector)
                find_residual(matrix, vector, solution)

                if result == 0:
                    print("Решений для данной матрицы не существует")
                else:
                    print("\nПолученные неизвестные векторы:", result)

                if np.allclose(solution, numpy_solution):
                    print(
                        "Решение, полученное с использованием сторонней библиотеки, совпадает с решением методом Гаусса.")
                    print(numpy_solution)
                else:
                    print("Решения, полученные разными методами, не совпадают.")

            except FileNotFoundError:
                print("Ошибка: Файл не найден")
                sys.exit()

            break

        else:
            print("Для ввода доступно только '1' или '2'")
            check_input_console()


check_input_console()

