from random import randint

def DigitSum(digit):
  return (digit % 10) + DigitSum(digit // 10) if digit != 0 else 0

for i in range(0, 6):
  num = randint(0, 100)
  print(f"Сума цифр числа {num} = {DigitSum(num)}")