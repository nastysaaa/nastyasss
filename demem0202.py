import random
print("Jums jauzmin skaitlis no intervāla [1; 10].")
dators = random.randint(1,10)
for i in range(1,11):
    lietotajs = int(input("Ievadi skaitli:"))
    if dators > lietotajs :
        print("Skaitlis ir lielaks")
    elif dators< lietotajs:
        print("Skaitlis ir mazāks")
    else:
        print("Uzminēts")
        break
print("Mēginājumu skaits:",i)