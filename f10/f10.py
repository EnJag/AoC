with open('f10/f10.txt') as fichier:
    contenu = fichier.readlines()
# print(contenu)
etats_attendus = []
boutons = []
voltages_attendus = []
for ligne in contenu:
    parts = ligne.strip().split()
    etat_str = parts[0].strip('[]')
    etats_attendus.append([0 if c == '.' else 1 for c in etat_str])
    boutons_ligne = []
    for bouton_str in parts[1:-1]:  # On ignore la dernière partie (joltage)
        bouton = [int(i) for i in bouton_str.strip('()').split(',')]
        boutons_ligne.append(tuple(bouton))
    boutons.append(boutons_ligne)
    voltage_str = parts[-1].strip("'{}'")
    voltages_attendus.append([int(i) for i in voltage_str.split(',')])

# # Partie 1
# from itertools import product

# max_presses = 2
# min_presses = []
# idx=0
# for etat_attendu, bouton_list in zip(etats_attendus, boutons):
#     idx+=1
#     print(idx/len(etats_attendus))
#     presses_liste = []
#     for presses in product(range(max_presses + 1), repeat=len(bouton_list)):
#         etat = [0] * len(etat_attendu)
#         nb_presses = 0
#         for i, button in enumerate(bouton_list):
#             for _ in range(presses[i]):
#                 for pos in button:
#                     etat[pos] = 1 - etat[pos]
#                 nb_presses += 1
#         if etat == etat_attendu:
#             presses_liste.append(nb_presses)
#     if presses_liste:
#         min_presses.append(min(presses_liste))
#     else:
#         min_presses.append(0)
# print(min_presses)
# print(sum(min_presses))

# Partie 2
import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds

def solve_joltage_equations(voltages_attendu, bouton_list):
    n_boutons = len(bouton_list)
    n_voltages = len(voltages_attendu)

    A = np.zeros((n_voltages, n_boutons), dtype=int)
    for i, button in enumerate(bouton_list):
        for j in button:
            A[j, i] = 1
    b = np.array(voltages_attendu)
    constraints = LinearConstraint(A, lb=b, ub=b)
    integrality = np.ones(n_boutons, dtype=int)
    bounds = Bounds(lb=0, ub=np.inf)
    res = milp(c=np.ones(n_boutons), constraints=constraints,
               integrality=integrality, bounds=bounds)

    if res.success:
        return int(res.fun)
    else:
        return None
    
min_presses = []
idx=0
for voltage_attendu, bouton_list in zip(voltages_attendus, boutons):
    min_presse = solve_joltage_equations(voltage_attendu, bouton_list)
    idx+=1
    print(f'{(idx/len(etats_attendus))*100:.2f}% | {min_presse}')
    min_presses.append(min_presse)
print(sum(min_presses))