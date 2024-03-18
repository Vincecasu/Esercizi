import json

#Per leggere un file json 
filejson = open("all-world-cup-players.json", "r")
worldcup = json.load(filejson)
filejson.close()

#Contare quanti calciatori hanno giocato per l'Italia:
'''
num_italian_players = 0

for v in worldcup:
    if v["Team"] == "Italy":
        num_italian_players += 1

print(f"I calciatori che hanno giocato per l'Italia  sono: {num_italian_players}")
'''

quantiCalciatori = dict()
for v in worldcup:
    # se v.Team è già presente, sommo 1, altrimenti metto a 1
    if v["Team"] in quantiCalciatori.keys():
        quantiCalciatori[v["Team"]]=quantiCalciatori[v["Team"]]+1
    else:
        quantiCalciatori[v["Team"]]=1

print(quantiCalciatori)

