import random
n = int(input("Cik elementu būs saraksta n="))
a = int(input("Mazākais iespejamais elements sarakstā a="))
b = int(input("Lielākais iespejamais elements sarakstā b="))
saraksts = list()
for i in range(n):
    skaitlis = random.randint(a,b)
    saraksts.append(skaitlis)
print(saraksts)
for i in range(n-1):
    if (saraksts[i] > 0 and saraksts [i+1] > 0) or (saraksts[i] < 0 and saraksts[i+1] < 0):
        print(saraksts[i], saraksts[i+1])
        break