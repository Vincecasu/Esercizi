numero = ""
virgola = False
while True:
    c = input ("Digita 0-9,+-/=: ")
    if len(c)>0:
        c = [0]
    if len(c)==0:
        continue

    if c not in ["0","1","2","3","4","5","6","7","8","9",","]:
        print("Il numero è: ",numero)
        break
    elif c==",":
        if not virgola:
            numero = numero + c
            virgola=True
        else:
            continue
    
    else:
        numero = numero + c