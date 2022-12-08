skaits = 0
while skaits < 5:
    skaitlis = int(input("Ievadi veselu skaitli="))
    if skaitlis == 0:
        continue 
    print("Ievadītais skaitlis ir", skaitlis)
    skaits += 1
else:
    print("Visi 5 skaitli ievadīti.") 
print("Programma beidz darbu !!!")