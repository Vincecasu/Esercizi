def GeneraListaDigit():
    lista = []
    for i in range(0,10000):
        s = str(i)
        while len(s) < 4 :
            s = "0" + s
        lista.append(s)
    return lista

print(GeneraListaDigit())


