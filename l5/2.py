import random

def double_factorial(n):
  if(n > 2):
    return n * double_factorial(n - 2)
  return n


for i in range(0, 5):
  num = random.randint(1, 10)
  print(f'Двойной факториал числа {num} = {double_factorial(num)}')
