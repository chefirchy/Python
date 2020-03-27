import math
a = int(input())
b = int(input())
x = int(input())
c = math.log(x**2+a*b, 10)
d = int()
d = c/7
if d>7:
    d= d/7
if d >=0 and d <1:
    d =+1
if d >=1 and d<2:
    print("Понедельник")
if d >=2 and d<3:
    print("Вторник")
if d >=3 and d<4:
    print("Среда")
if d >=4 and d <5:
    print("Четверг")
if d >=5 and d <6:
    print("Пятница")
if d >=6 and d <7:
    print("Суббота")
if d >=7:
    print("Воскресенье")