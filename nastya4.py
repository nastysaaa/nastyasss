import random
n = int(input("Cik elementu būs saraksta n="))
a = int(input("Mazākais iespejamais elements sarakstā a="))
b = int(input("Lielākais iespejamais elements sarakstā b="))
saraksts = list()
for i in range(n):
    skaitlis = random.randint(a,b)
    saraksts.append(skaitlis)
print(saraksts)
skaits = 0
for i in range(n-2):
    if saraksts[i] < saraksts[i+1] > saraksts[i+2]:
        skaits += 1
    print(skaits)