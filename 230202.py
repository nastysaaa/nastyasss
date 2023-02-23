import random
print("Ievadi: a - Akmens / s - Škēres / p - Papīrītis")
luzv = 0
duzv = 0
for t in range(10):
    liet = input("Tava izvēle ==> ")
    dat = random.choice("asp")
    print("Datora izvēle ==>",dat)
    if liet == dat:
        print("Neizšķirts!")
    elif (liet=="a"and dat=="s") or (liet=="s" and dat=="p") or (liet== "p" and dat=="a"):
        print("Vinnēja lietotājs!")
        luzv += 1
    else:
        print("Vinnēja dators!")
        duzv += 1
if duzv > 1:
    print("Kopumā vinnēja dators!")
elif duzv < 1:
    print("Kopumā vinnēja lietot;ajs!")
else:
    print("Kopumā neizšķirts!")