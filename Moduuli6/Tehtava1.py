import random
def heitä_noppaa():
    silmäluku = random.randint(1, 6)
    return silmäluku
while True:
    tulos = heitä_noppaa()
    print(tulos)
    if tulos == 6:
        break