# 6) Trovare qual'è il calciatore più giovane che ha partecipato alla coppa 
# del mondo

import json
#Per leggere un file json:

filejson = open("all-world-cup-players.json","r")
worldcup =json.load(filejson)
filejson.close()

listaAnno = []

calciatorepiùgiovane = []

for c in worldcup:
    listaAnno.append(int(c["DateOfBirth"]))
print(listaAnno)
   
    

    