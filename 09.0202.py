import random 
maks = int(input("Ievadi maksimaļo skaitli="))
print("Jums jāuzmin skaitlis no intervāla [1; maks].")
dators = random.randint(1, maks)
for i in range(1,maks+1):
    lietotajs = int(input("Ievadi mināmo skaitli="))
    if lietotajs < dators: 
        print("Mans skaitlis ir lielāks!")
    elif lietotajs > dators:
        print("Mans skaitlis ir mazāks!")
    else:
        print("Uzminēts!")
        break
print("Mēginājumu skaits:",i)