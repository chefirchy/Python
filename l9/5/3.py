str_reversed=""
try:
 with open('file.txt','r') as f:
  str_reversed=f.read()[::-1]
except FileNotFoundError:
 print("File not found")
 print('File not found. Do you want create new file?')
 a=int(input('1-yes, 0- no\n'))
 if a==1:
        f = open('text.txt', 'w')
        print('File created \nInput data in file')
        stop=False
        print('if you want stop input input 0')
        str=""
        while True!=stop:
          a=input()
          if a!='0':
              str=str+a+'\n'
          else:
             str=str[0:len(str)-1]
             stop=True
        f.write(str)
        str_reversed=str[::-1]
f=open('text_reversed.txt','w')
f.write(str_reversed)