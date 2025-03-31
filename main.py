import math


def calculate_S(n):
    h1 = math.sqrt(2) / 2 / n
    s1 = sum(math.asin(i * h1) for i in range(1, n+1)) * h1

    h2 = (1 - math.sqrt(2) / 2) / n
    s2 = sum(math.acos(math.sqrt(2) / 2 + i * h2) for i in range(1, n+1)) * h2

    return s1 + s2


print(f"Точное вычисление: {math.sqrt(2) - 1}")
print(f"n=10: {calculate_S(10)}")
print(f"n=100: {calculate_S(100)}")
print(f"n=1000: {calculate_S(100)}")
