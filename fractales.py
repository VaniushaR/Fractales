# --- FRACTAL CON CIRCULOS --
from turtle import *
pensize(1)
speed(0)


def circlePR(x, y, r):
    sx = x
    sy = y - r
    penup()
    goto(sx, sy)
    pendown()
    circle(r)


def drawCircle(x, y, r):
    circlePR(x, y, r)
    if r > 2:
        drawCircle(x + r, y, r/2)
        drawCircle(x - r, y, r/2)


drawCircle(0, 0, 600)
done()

# --- FIN FRACTAL CON CIRCULOS ---


# --- EXPONENCIAL ITERATIVA --
def pow(base, exp):
    ans = 1
    if exp <= 0:
        return 1
    while exp >= 1:
        ans *= base
        exp -= 1
    return ans


print(pow(2, 3))

# --- FIN EXPONENCIAL ITERATIVA ---


# --- EXPONENCIAL RECURSIVA ---
def powRecursive(base, exp):
    if exp <= 0:
        return 1
    else:

        return base * powRecursive(base, exp-1)


print(powRecursive(2, 3))
# --- FIN EXPONENCIAL RECURSIVA ---


# --- FIBONACCI RECURSIVO BINARIO (MUY INEFICIENTE) ---


# Fibonacci
# F0 = 0
# F1 = 1
# Fn = F[n-1] + F[n-2]

# Fibonacci con recursion binaria
def fibonacci(k):
    if k == 0:
        return 0
    if k == 1:
        return 1
    return fibonacci(k-1) + fibonacci(k-2)


print(fibonacci(9))

# --- FIBONACCI RECURSIVO LINEAL (MUY RAPIDO)---

# Fibonacci con recursion lineal


def fibonacciLinear(k):
    if k <= 1:
        return [k, 0]
    else:
        x = fibonacciLinear(k-1)
        return [x[0] + x[1], x[0]]


print(fibonacciLinear(4)[0])

# UNAMDevChallenge
