def evclid(a, b):
  if(b == 0):
    return a
  if(a == 0):
    return b
  if(a > b):
    return evclid(a % b, b)
  return evclid(a, b % a)

num1 = 2
num2 = 5
num3 = 8
num4 = 10

print('НСД 1 и 2 числа: ', evclid(num1, num2))
print('НСД 3 и 4 числа: ', evclid(num3, num4))
print('НСД 1 и 4 числа: ', evclid(num1, num4))