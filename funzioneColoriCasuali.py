#Scrivere una funzione ColoreCasuale() che torna una stringa
# casuale tra "rosso","giallo","verde","blu","arancio","ciano","rosa",
# "turchese", e cosi via ,...

import random


def ColoreCasuale():
    colori = ["rosso","giallo","verde","blu","arancio","ciano","rosa",
              "turchese"]
    for i in colori:
        colori.append (random.randint(len(0,i)))
        
        return colori

print(ColoreCasuale())