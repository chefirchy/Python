a, b, c, d = map(int, input("Введите x1, y1, x2, y2: ").split())  # a == x1, b == y1, c == x2, d == y2
A = abs(c - a); B = abs(d - b)
P = 2*(A+B); S = A*B
print("Периметр = {0}, Площадь = {1}".format(P, S))