print("Умова: Знайти найменше ціле число K, при якому виконується нерівність 3K > N.")
n = int(input("Значення「N」: ")); k = int(1)
while 3*k <= n:
    k+=1
print("【НЦЧ k】 => {0}".format(k))
