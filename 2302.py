import random
print("Ievadi: a - Akmens / s - Škēres / p - Papīrītis")
liet = input("Tava izvēle ==> ")
dat = random.choice("asp")
print("Datora izvēle ==>",dat)
if liet == dat:
        print("Neizšķirts!")
elif (liet=="a"and dat=="s") or (liet=="s" and dat=="p") or (liet== "p" and dat=="a"):
    print("Vinnēja lietotājs!")
else:
    print("Vinnēja dators!")