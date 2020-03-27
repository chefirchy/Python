def get_reversed():
  number = input('Введите число из последовательности, если хотите остановиться - введите 0 ')
  if(number == '0'):
    return ''
  return number + get_reversed()

def print_reversed():
  print(get_reversed())

print_reversed()