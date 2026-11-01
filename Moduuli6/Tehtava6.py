
import math
def laske_yksikköhinta(halkaisija, hinta):
    säde = halkaisija / 2 / 100
    pinta_ala = math.pi * säde ** 2
    return hinta / pinta_ala
halkaisija1 = float(input("Anna ensimmäisen pizzan halkaisija (cm): "))
hinta1 = float(input("Anna ensimmäisen pizzan hinta (€): "))
halkaisija2 = float(input("Anna toisen pizzan halkaisija (cm): "))
hinta2 = float(input("Anna toisen pizzan hinta (€): "))
yksikköhinta1 = laske_yksikköhinta(halkaisija1, hinta1)
yksikköhinta2 = laske_yksikköhinta(halkaisija2, hinta2)
print("Pizza 1:", round(yksikköhinta1, 2), "€/m²")
print("Pizza 2:", round(yksikköhinta2, 2), "€/m²")
if yksikköhinta1 < yksikköhinta2:
    print("Pizza 1 antaa paremman vastineen rahalle.")
elif yksikköhinta2 < yksikköhinta1:
    print("Pizza 2 antaa paremman vastineen rahalle.")
else:
    print("Molemmat pizzat ovat yhtä edullisia.")
