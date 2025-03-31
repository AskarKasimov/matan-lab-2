import math

a, b = list(map(int, input("Введите a и b (через пробел): ").split()))
exact = 2*math.pi*a**2 + 4*math.pi*b**2

for n in [10, 100, 1000]:
    s = 0
    dO = 2*math.pi/n
    for i in range(n):
        O = i*dO
        r = 2*a*math.cos(O) + 2*b
        s += r**2
    approx = 0.5 * s * dO
    print(f"n={n}: {approx}")
