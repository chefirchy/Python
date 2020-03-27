#Опять файл кину в папку(Такая же проблема)
import re

def get_file_content():
  f = open('C:/Users/chefi/Documents/tfile.txt', 'r')
  file_content = f.read()
  f.close()
  words_arr = []
  for word in re.split(r'\s+', file_content):
    words_arr.append(word.lower())
  return words_arr

def count_unique_words():
  words_arr = get_file_content()
  count = 0
  considered = {}
  for word in words_arr:
    if(word not in considered):
      considered[word] = True
      count += 1
  return int(count)

print('Количество слов в строке ', len(get_file_content()))
print('Количество уникальных слов в строке ', count_unique_words())