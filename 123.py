skaitlis = int(input("Ievadi skaitli: "))
lielakais = skaitlis
mazakais = skaitlis
skaits = 1
while skaits <= 10 and skaitlis != 0:
    skaitlis = int(input("Ievadi skaitli: "))
    if skaitlis > lielakais:
        lielakais = skaitlis
    if skaitlis < mazakais:
        mazakais = skaitlis
    skaits += 1
print("Lielakais skaitlis ir", lielakais)
print("Mazakais skaitlis ir", mazakais)
