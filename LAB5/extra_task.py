import numpy as np

def stirling_interpolation(x, y, x_interp):
    n = len(x)
    h = x[1] - x[0]
    s = (x_interp - x[n//2]) / h

    delta = np.zeros((n, n))
    delta[:, 0] = y

    for j in range(1, n):
        for i in range(n - j):
            delta[i, j] = delta[i + 1, j - 1] - delta[i, j - 1]

    y_interp = delta[n//2, 0]
    fact = 1
    for i in range(1, n):
        if i % 2 == 1:
            term = (s - (i//2)) / i
        else:
            term = (s + (i//2)) / i
        fact *= term
        y_interp += fact * delta[(n - i)//2, i]

    return y_interp


def bessel_interpolation(x, y, x_interp):
    n = len(x)
    h = x[1] - x[0]
    s = (x_interp - x[n//2]) / h

    delta = np.zeros((n, n))
    delta[:, 0] = y

    for j in range(1, n):
        for i in range(n - j):
            delta[i, j] = delta[i + 1, j - 1] - delta[i, j - 1]

    y_interp = (delta[n//2, 0] + delta[n//2 - 1, 0]) / 2
    fact = 1
    for i in range(1, n):
        if i % 2 == 1:
            term = (s - (i//2)) / i
        else:
            term = (s + (i//2)) / i
        fact *= term
        y_interp += fact * (delta[(n - i)//2, i] + delta[(n - i)//2 - 1, i]) / 2
    return y_interp
