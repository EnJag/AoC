with open("f2/f2.txt", "r") as fichier:
    contenu = fichier.read()
    l = [r for r in contenu.split(',')]
    count = 0
    for el in l:
        print('_____')
        print(el)
        debut = int(el.split('-')[0])
        fin = int(el.split('-')[1])
        for i in range(debut, fin+1):
            i = str(i)
            length = len(i)
            # trouver les diviseurs de length
            div = [d for d in range(1, length) if length%d==0]
            # créer les sous-listes avec chaque diviseur
            lb = [[i[j:j+pas] for j in range(0, len(i), pas)] for pas in div]
            # vérifier si une des sous-listes a tous les éléments identiques
            for sublist in lb:
                if all(x == sublist[0] for x in sublist):
                    if len(sublist) > 2:
                        print(i)
                    count += int(i)
                    # une fois qu'on a trouvé un diviseur qui marche, on peut s'arrêter
                    break

    print(count)