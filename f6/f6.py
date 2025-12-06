def mul(liste):
    res=1
    for nb in liste:
        res*=nb
    return res

with open('f6/f6.txt') as fichier:
    contenu = fichier.read()
    liste = [ligne for ligne in contenu.splitlines()]
    operations = [op for op in liste[-1] if op=='+' or op=='*']
    nb_ligne = len(liste)-1
    nb_colonne = len([nb for nb in liste[0].split(' ') if nb!=''])
    print(nb_colonne, nb_ligne)
    liste_propre = [[nb for nb in liste[i].split(' ') if nb!=''] for i in range(nb_ligne)]
    liste_ordre = []
    for i in range(nb_colonne):
        temp = []
        for j in range(nb_ligne):
            temp.append(int(liste_propre[j][i]))
        liste_ordre.append(temp)
    total_1=0
    for nb, op in zip(liste_ordre, operations):
        if op=='+':
            total_1+=sum(nb)
        else:
            total_1+=mul(nb)
    print(total_1)

    derniere_ligne = [op for op in liste[-1]]
    ecarts=[]
    temp=0
    for el in derniere_ligne[1:]:
        if el=='*' or el=='+':
            ecarts.append(temp)
            temp=0
        else:
            temp+=1
    ecarts.append(temp+1)    
    nb_colonne = len([nb for nb in liste[0]])
    liste_propre = [[nb for nb in liste[i]] for i in range(nb_ligne)]
    liste_ordre = []
    for i in range(nb_colonne):
        temp = []
        for j in range(nb_ligne):
            temp.append(liste_propre[j][i])
        liste_ordre.append(temp)
    liste_ordre = [item for item in liste_ordre if item != [' ' for i in range(nb_ligne)]]
    for i in range(len(liste_ordre)):
        s=''
        for j in range(nb_ligne):
            if liste_ordre[i][j]!=' ':
                s+=liste_ordre[i][j]
        liste_ordre[i]=int(s)
    liste_ordre_2=[]
    index=0
    for ecart in ecarts:
        liste_ordre_2.append(liste_ordre[index:index+ecart])
        index+=ecart
    print(len(liste_ordre_2), len(operations))
    total_2=0
    for nb, op in zip(liste_ordre_2, operations):
        if op=='+':
            total_2+=sum(nb)
        else:
            total_2+=mul(nb)
    print(total_2)

