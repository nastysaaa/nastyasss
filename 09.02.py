import random
print("Jums jāuzmin skaitlis no intervāla [1; 10].")
dators = random.randint(1, 10)
for i in range(1,11):
    lietotajs = int(input("Ievadi mināmo skaitli="))
    if lietotajs < dators: 
        print("Mans skaitlis ir lielāks!")
    elif lietotajs > dators:
        print("Mans skaitlis ir mazāk!")
    else:
        print("Uzminēts!")
        break
print("Mēginājumu skaits:",i)