oikea_tunnus = "daniel_oksanen"
oikea_salasana = "pythontehtava5"
while True:
    tunnus = input("Anna käyttäjätunnus: ")
    salasana = input("Anna salasana: ")
    if tunnus == oikea_tunnus and salasana == oikea_salasana:
        print("Tervetuloa")
        break
    else:
        print("Pääsy evätty")