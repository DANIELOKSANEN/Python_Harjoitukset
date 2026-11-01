
def laske_summa(luvut):
    summa = 0
    for luku in luvut:
        summa = summa + luku
    return summa
luvut = [2, 5, 8, 10, 15]
tulos = laske_summa(luvut)
print("Lukujen summa:", tulos)
