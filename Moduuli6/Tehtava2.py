import random
def heitä_noppaa(tahkot):
    silmäluku = random.randint(1, tahkot)
    return silmäluku
tahkot = int(input("Anna nopan tahkojen määrä: "))
while True:
    tulos= heitä_noppaa(tahkot)
    print(tulos)
    if tulos == tahkot:
        break
