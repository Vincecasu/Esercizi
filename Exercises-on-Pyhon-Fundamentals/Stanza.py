## In una stanza entrano, uno dopo l'altro, 10 persone, rispettivamente:
# anita, annarita, lucia, antonio, marco, andrea, luigi, tony, bruno, laura, 
# le prime due vanno via dopo un pochino di tempo ma entrano altre tre persone
# john, alice, mary
# altre due vanno via, sempre in ordine di ingresso (primo entrato, primo a uscire)
# stampare l'elenco delle persone presenti
## infine, stampare le persone presenti in ordine alfabetico

stanza = ["anita", "annarita", "lucia" , "antonio", "marco", "andrea", "luigi",
          "tony", "bruno", "laura",]

print (stanza)

stanza = stanza [2 :]
print (stanza)

stanza.append ("john")
stanza.append ("alice")
stanza.append ("mary")

print (stanza)

stanza.sort()

print (stanza)
