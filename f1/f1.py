with open("f1/f11.txt", "r") as fichier:
    contenu = fichier.read()
    l = [ligne for ligne in contenu.splitlines()]
    dial = 50
    count = 0
    for el in l:        
        amount = int(el[1:])

        # retire les tours complets
        count += amount//100
        amount %= 100

        if el[0] == "R":
            dial += int(amount)
        else:
            dial -= int(amount)

        # pour le cas ou on passe par 0 par R
        if dial > 100:
            count += 1

        # pour le cas ou on passe par 0 par L en enlevant le cas où on part de 0
        if dial < 0 and dial+int(amount) != 0:
            count += 1
        dial %= 100

        # pour le cas ou on arrive a 0
        if dial == 0:
            count += 1
            
    print(count)