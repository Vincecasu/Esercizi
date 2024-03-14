def Converti(s):

    usaMetodo1 = False

    if usaMetodo1:
     #con la Comprehension:
         
     return[int(c) for c in s]
    
    else:
       #Metodo 2 , con for

       l = list(s)
       l1 = []
       for i in l:
          l1.append(int(i))
    return l1

print(Converti("192619263183"))