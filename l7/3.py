import re

text: str = "1 2 3 4"

nums: list = re.findall(r'\d', text)

max_num = max(nums)

numers_tuple = ('Ноль', 'Один', 'Два', 'Три', 'Четыре', 'Пять', 'Шесть', 'Семь', 'Восемь', 'Девять')

text = text.replace(max_num, numers_tuple[int(max_num)])

print(f'Видоизмененная строка:\n {text}')