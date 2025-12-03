with open('f3/f3.txt') as fichier:
    contenu = fichier.read()
    liste = [[int(nombre) for nombre in ligne] for ligne in contenu.splitlines()]

    total_1=0
    for bank in liste:
        print('___')
        print(bank)
        premier = max(bank)
        index_premier = bank.index(premier)
        # c'est le dernier élément
        if index_premier == len(bank)-1:
            # supprime le dernier élément
            bank.pop()
            second = max(bank)
            # permutons pour garder l'ordre
            premier, second = second, premier
        else:
            second = max(bank[index_premier+1:])
        jolt_max = int(str(premier) + str(second))
        print(jolt_max)
        total_1 += jolt_max
    print(total_1)

    """
    Approche 1 :
    1. Trier le dictionnaire des indices et des valeurs par valeur croissante et par indice décroissant.
    2. Prendre les 12 derniers.
    3. Retrier par les indices.
    """
    # total_2=0
    # for bank in liste:
    #     print('___')
    #     print(bank)
    #     dictionnaire = {idx:el for idx,el in enumerate(bank)}
    #     dictionnaire = dict(sorted(dictionnaire.items(), key = lambda x: (x[1], x[0])))
    #     dictionnaire = dict(list(dictionnaire.items())[-12:])
    #     dictionnaire = dict(sorted(dictionnaire.items(), key = lambda x: x[0]))
    #     liste_finale = list(dictionnaire.values())
    #     s = ''
    #     for nombre in liste_finale:
    #         s += str(nombre)
    #     print(int(s))
    #     total_2 += int(s)
    # print(total_2) # 147003179153108

    """
    Approche 2 :
    1. Prendre les 12 nombres les plus à droite.
    2. Les déplacer au maximum le plus à gauche.
    3. Couper la liste des prospects après le nouveau maximum trouvé.
    """
    # total_2=0
    # for bank in liste:
    #     print('_____________')
    #     print(bank)
    #     dictionnaire = {idx:el for idx,el in enumerate(bank)}
    #     # les 12 derniers éléments
    #     dictionnaire_12 = dict(list(dictionnaire.items())[-12:])
    #     for index,i in zip(dictionnaire_12.keys(),range(len(dictionnaire_12))):
    #         dictionnaire_gauche = {idx:el for idx,el in dictionnaire.items() if idx not in dictionnaire_12.keys() and idx<index} if i == 0 else {idx:el for idx,el in dictionnaire.items() if idx not in dictionnaire_12.keys() and idx>min(dictionnaire_12.keys()) and idx<index}
    #         if len(dictionnaire_gauche)>0 and dictionnaire_12[index]<=max(dictionnaire_gauche.values()):
    #             dictionnaire_12[list(dictionnaire_gauche.keys())[list(dictionnaire_gauche.values()).index(max(dictionnaire_gauche.values()))]]=max(dictionnaire_gauche.values())
    #             dictionnaire_12.pop(index)
    #         else:
    #             break
    #     dictionnaire_12 = dict(sorted(dictionnaire_12.items(), key = lambda x: x[0]))
    #     dictionnaire = dict(sorted(dictionnaire_12.items(), key = lambda x: x[0]))
    #     liste_finale = list(dictionnaire_12.values())
    #     s = ''
    #     for nombre in liste_finale:
    #         s += str(nombre)
    #     print(int(s))
    #     total_2 += int(s)
    # print(total_2) # 170230853712328

    """
    Approche 3 (bon résultat):
    1. Pour chaque nombre de la sous-liste des 12 derniers, trouver le maximum entre l'indice du dernier maximum trouvé et lui-même.
    """
    total_2 = 0
    for bank in liste:
        print('_____________')
        print(bank)
        liste_finale = []
        for i in range(12):
            maximum_trouve = max(bank[:-11+i]) if -11+i !=0 else max(bank)
            liste_finale.append(maximum_trouve)
            bank = bank[bank.index(maximum_trouve)+1:]
        s = ''
        for nombre in liste_finale:
            s += str(nombre)
        print(int(s))
        total_2 += int(s)
    print(total_2) # 172981362045136
