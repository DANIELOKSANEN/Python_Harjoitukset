import random
määrä= int(input("Anna arpakuutioiden lukumäärä: "))
summa= 0
for i in range(määrä):
    heitto= random.randint(1, 6)
    summa += heitto
print("silmälukujen summa on:", summa)