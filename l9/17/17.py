f=open('p.txt','r')#p-пустой файл. Чтобы получить файл с результатами, то заменить р на о
lines=f.read().split('\n')
matrix=[]
for line in lines:
    print(line)
    matrix.append(line.split('|'))
i = int(input('Input i (0 :{0})\n'.format(len(matrix)-1)))
j = int(input('Input j (0 :{0})\n'.format(len(matrix[0])-1)))
try:
    print(matrix[i][j])
except IndexError:
    print("You are out of range")