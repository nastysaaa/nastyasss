import random
lsumma = 0 
for i in range(10):
    k1 = random.randint(1,6)
    k2 = random.randint(1,6)
    if k1 > k2:
       lielakais = k1
    else:
       lielakais = k2
    summa = k1 + k2
    if summa > lsumma:
        lsumma = summa
    print(k1, k2, "|", lielakais, "|", summa)
print("Lielaka summa ir:", lsumma)