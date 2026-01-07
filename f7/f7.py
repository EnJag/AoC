with open('f7/f7.txt') as fichier:
    contenu = fichier.read()
    liste = [[word for word in ligne] for ligne in contenu.splitlines()]
    nb_ligne = len(liste)
    nb_colonne = len(liste[0])
    '''
    Hypothèse fausse :
    il y a un split sur un spliter dès lors qu'un spliter est situé juste à droite où juste à gauche et 2 rangs au-dessus de celui-ci.
    '''
    # split=1 # ligne 2 obligatoire qu'on va ignorer par la suite
    # for idx_l, ligne in enumerate(liste):
    #     if idx_l>3:
    #         for idx_c, char in enumerate(ligne):
    #             if char=='^':
    #                 if idx_c-1 >= 0 and liste[idx_l-2][idx_c-1]=='^': # gauche
    #                     split+=1
    #                     print(idx_l,idx_c)
    #                     continue # pour pas compter deux fois
    #                 if idx_c+1 <= nb_colonne+1  and liste[idx_l-2][idx_c+1]=='^': # droite
    #                     split+=1
    #                     print(idx_l,idx_c)
    # print(split) # 1618

    '''
    First star
    '''
    split=0
    for idx_l, ligne in enumerate(liste):
            for idx_c, char in enumerate(ligne):
                if liste[idx_l-1][idx_c]=='S' or (liste[idx_l-1][idx_c]=='|' and liste[idx_l][idx_c]!='^'):
                    liste[idx_l][idx_c]='|'
                elif char=='^':
                    if liste[idx_l-1][idx_c]=='|':
                          split+=1
                    liste[idx_l][idx_c-1], liste[idx_l][idx_c+1] = '|', '|'
    for ligne in liste:
        print(ligne)
    print(split) # 1656

    '''
    Second star
    '''
    liste = [[word if word!='.' else 0 for word in ligne] for ligne in contenu.splitlines()]
    for idx_l, ligne in enumerate(liste):
            for idx_c, char in enumerate(ligne):
                if idx_l>0 and idx_l<len(liste)-1 and idx_c>0 and idx_c<len(ligne)-1: 
                    if liste[idx_l-1][idx_c]=='S':
                        liste[idx_l][idx_c]=1
                    if liste[idx_l][idx_c]!='^' and liste[idx_l][idx_c]!='S':
                        if liste[idx_l][idx_c]>0:
                            if liste[idx_l+1][idx_c]!='^':
                                liste[idx_l+1][idx_c]+=liste[idx_l][idx_c]
                            else:
                                liste[idx_l+1][idx_c-1]+=liste[idx_l][idx_c]
                                liste[idx_l+1][idx_c+1]+=liste[idx_l][idx_c]
    for col in range(len(liste[-1])): # dernière ligne pour prendre en compte la première et la dernière colonne
        liste[-1][col] = liste[-2][col] if liste[-2][col]!='^' else 0

    for ligne in liste:
         print([str(x) for x in ligne])
    print(sum([x for x in liste[-1] if x!='.'])) # 76624086587804