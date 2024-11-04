# def factorial(n):
#     number = 1
#     for i in range (n, 0, -1):
#         number *= i
#     return number


def factorial(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return factorial(n-1)*n
