print("Programma uzminēs skaitli no intervāla [m; n].")
m = int(input("Ievadi m="))
n = int(input("Ievadi n="))
meginajumi = 0
atminets = False 
while atminets == False:
    skaitlis = (m + n)//2
    print("Vai iedomātais skitlis ir", skaitlis)
    meginajumi += 1
    atbilde = input("Atbildi: m - ja tavs skaitlis mazāks, l - ja lielāks, u - ja uzminēts:")
    if atbilde == "m":
        n = skaitlis
    elif atbilde == "l":
        m = skaitlis 
    else: 
        atminets = True
print("Meginājumu skaits:", meginajumi)