with open('f4/f4.txt') as fichier:
    contenu = fichier.read()
    liste = [[1 if word=='@' else 0 for word in ligne] for ligne in contenu.splitlines()]
    print(len(liste), len(liste[0]))
    # ajout padding
    liste.insert(0,[0 for i in range(len(liste[0]))])
    liste.append([0 for i in range(len(liste[0]))])
    for sublist in liste:
        sublist.insert(0,0)
        sublist.append(0)
    print(len(liste), len(liste[0]))

    total_2=0
    tour=0
    sous_total = None
    while sous_total != 0:
        sous_total=0
        for row in range(len(liste)):
            for column in range(len(liste[row])):
                if liste[row][column]==1:
                    voisin = []
                    for i in range(-1,2,1):
                        for j in range(-1,2,1):
                            voisin.append(liste[row+i][column+j])
                    if sum(voisin)<=4:
                        sous_total+=1
                        liste[row][column]=0
        total_2 += sous_total
        tour += 1
        print(f'tour : {tour} | sous total : {sous_total}')
    print(total_2)
