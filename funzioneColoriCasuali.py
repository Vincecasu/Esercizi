#Scrivere una funzione ColoreCasuale() che torna una stringa
# casuale tra "rosso","giallo","verde","blu","arancio","ciano","rosa",
# "turchese", e cosi via ,...

import random


def ColoreCasuale():
    colori = ["rosso","giallo","verde","blu","arancio","ciano","rosa",
              "turchese"]
       
    return colori[random.randint(0,len(colori)-1)]

print(ColoreCasuale())