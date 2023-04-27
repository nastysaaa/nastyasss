import random
n = int(input("Cik elementu būs saraksta n="))
a = int(input("Mazākais iespejamais elements sarakstā a="))
b = int(input("Lielākais iespejamais elements sarakstā b="))
saraksts = list()
for i in range(n):
    skaitlis = random.randint(a,b)
    saraksts.append(skaitlis)
print(saraksts)
for i in range(n):
    neatk = True
    for j in range(n):
        if saraksts[i] == saraksts[j] and i != j:
                neatk = False
                break
        if neatk == True:
             print(saraksts[i], end=" ")