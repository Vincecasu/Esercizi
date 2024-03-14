#Modificare la GeneraListaDigit per generare una Lista di Liste del tipo
#[[0,0,0,0],[0,0,0,1],[0,0,0,2],...,[9,9,9,8],[9,9,9,9]]

def GeneraListaDigit():

    lista = []
    for i in range(0,10000):
        s = str(i)
        while len(s) < 4:
            s = "0" + s
#Ora Devo modificare s in lista di Digit
# s,esempio, è "3410" => [3,4,1,0]
        l1 = []
        for c in (s):
            l1.append(int(c))
        lista.append(l1)
    return lista

print(GeneraListaDigit())
