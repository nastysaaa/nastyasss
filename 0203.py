import random
summa_a =0
summa_j =0
sp_beigas = False
while sp_beigas == False:
    ka = random.randint(1,6)
    summa_a += ka
    kj = random.randint(1,6)
    summa_j += kj
    if summa_a >= 100 or summa_j >= 100:
        sp_beigas = True
    if summa_a > 100:
        summa_a = 0
    if summa_j > 100:
        summa_j = 0
if summa_a == summa_j:
    print("Neizšķirts!")
elif summa_a > summa_j:
    print("Vinnēja Anna!")
else:
    print("Vinnēja Jānis!")
    print("Punktu skaits Anna!:",summa_a)
    print("Punktu skaits Jānis!:",summa_j)