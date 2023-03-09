import random
jsumma = 0
asumma= 0
while jsumma < 100 and asumma <100:
    janis = random.randint(1,6)
    jsumma += janis
    anna = random.randint(1,6)
    asumma += anna
print("Jānis ieguva:",jsumma)
print("Anna ieguva:",asumma)
if jsumma > asumma:
    print("Vinēja Janis")
elif asumma > jsumma:
    print("Vinnēja Anna")
else:
    print("Neizšķirts")