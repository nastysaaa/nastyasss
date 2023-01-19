n = int(input("Ievadi n="))
s1 = 0 
for i in range(1, n+1):
    s1 += i
s2 = 0
for k in range(1, n):
    knr = int(input("Īevadi kārts nr.==>"))
    s2 += knr
print ("Pazudusī kārts ir" , s1 - s2)