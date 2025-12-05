with open('f5/f5.txt') as fichier:
    contenu = fichier.read()
    liste = [ligne for ligne in contenu.splitlines()]

    fresh_ids = [el for el in liste if '-' in el]
    ids = [int(el) for el in liste if '-' not in el and el != '']
    fresh_ingredients = [ingredient for intervalle in fresh_ids for ingredient in ids if ingredient in range(int(intervalle.split('-')[0]), int(intervalle.split('-')[1])+1)]
    reponse_1 = len(set(fresh_ingredients))
    print(reponse_1)

    petits_intervalles = [[int(el.split('-')[0]), int(el.split('-')[1])] for el in liste if '-' in el]
    petits_intervalles = sorted(petits_intervalles)
    grands_intervalles = [petits_intervalles[0]]
    for petit in petits_intervalles[1:]:
        print(f'PETIT : {petit}_____________')
        for grand in grands_intervalles:
            passe=0
            print(f'GRAND : {grand}_____________')
            if petit[0] >= grand[0] and petit[0] <= grand[1] and petit[1] >= grand[1]:
                grand[1] = petit[1]
                print('1', grand)
                passe=1
                break
            elif petit[1] >= grand[0] and petit[1] <= grand[1] and petit[0] <= grand[0]:
                grand[0] = petit[0]
                print('2',grand)
                passe=1
                break
            elif petit[0] >= grand[0] and petit[1] <= grand[1]:
                print('4')
                passe=1
                continue
            elif petit[0] <= grand[0] and petit[1] >= grand[1]:
                grand[0], grand[1] = petit[0], petit[1]
                print('3',grand)
                passe=1
                break
        if passe != 1:
            print(f'ajout de {petit}')
            grands_intervalles.append(petit)

    print(grands_intervalles)
    total_2=0
    for intervalle in grands_intervalles:
        total_2 += intervalle[1]-intervalle[0]+1
    print(total_2)