import random
n = int(input("Cik elementu būs saraksta n="))
a = int(input("Mazākais iespejamais elements sarakstā a="))
b = int(input("Lielākais iespejamais elements sarakstā b="))
saraksts = list()
for i in range(n):
    skaitlis = random.randint(a,b)
    saraksts.append(skaitlis)
print(saraksts)
skaits=0
for i in range(n-1):
    for j in range(i+1,n):
        if saraksts[i] == saraksts[j]:
            skaits += 1
print(skaits)
