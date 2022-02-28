import random

antall = int(input('Hvor mange skal trekkes? '))
navn = ['Marius', 'Haidas', 'Mantas', 'Bendik', 'Markus', 'Kevin', 'Benjamin', 'Robin', 'William', 'Johannes', 'Eirik','Liam', 'Romandus']

def trekk_tilfeldig(n):
    trekk = random.sample(navn, n)
    return trekk

#print(trekk_tilfeldig(antall))
utvalg = trekk_tilfeldig(antall)

for person in utvalg:
    print(person)


