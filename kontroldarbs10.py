import random
saraksts = [random.randint(1,100) for i in range(10)]
print(saraksts)
if 5 in saraksts:
    print("Skaitlis 5 atrodas sarakstā.")
else:
    print("Skaitlis 5 neatrodas sarakstā.")