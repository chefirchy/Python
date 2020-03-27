import re

def get_country_city():
  line = input('Введите страну(на первом месте и ее города) ')
  words_arr = line.split(' ')
  return words_arr

isNeedContinue = True

country_city_dict = {}

while True:
  words_arr: list = get_country_city()
  country = words_arr[0]
  words_arr.remove(words_arr[0])
  country_city_dict[country] = words_arr

  if(input('Если хотите остановится введите 0 ') == '0'):
    break 

print('Словарь стран и городов', country_city_dict)