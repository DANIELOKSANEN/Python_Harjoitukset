pituus = float(input("Anna kuhan pituus senttimetreinä: "))
if pituus < 37:
    puuttuu = 37 - pituus
    print("Kuha on alamittainen.")
    print(f"Laske kuha takaisin järveen. Pyyntimitasta puuttuu {puuttuu} cm.")
else:
    print("Kuha täyttää pyyntimitan.")