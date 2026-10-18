luvut= []
while True:
    syöte= input("Anna luku: ")
    if syöte=="":
        break
    luvut.append(float(syöte))
luvut.sort(reverse=True)
for luku in luvut [:5]:
    print(luku)