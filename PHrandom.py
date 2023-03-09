import random
sum = 0
mskaits = 0
while sum < 100:
    kaulins = random.randint(1, 6)
    sum += kaulins
    mskaits += 1
    print("Uzmesta",mskaits,"reize. Rezultats:", kaulins)
print("Sasniegta summa 100 ar", mskaits,"meiteniem")