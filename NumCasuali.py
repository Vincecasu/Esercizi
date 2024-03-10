import random


l1=[]

for i in range(5):
    l1.append(random.randint(1,1000))

print(l1)

totale = 0
for i in l1:
    totale = totale + i

print("totale: ", totale)