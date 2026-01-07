def dist_eucl_3d(j1,j2):
    dx = j1[0] - j2[0]
    dy = j1[1] - j2[1]
    dz = j1[2] - j2[2]
    return (dx**2 + dy**2 + dz**2)**(1/2)

with open(('f8/f8.txt')) as fichier:
    contenu = fichier.read()

liste = [[int(el) for el in ligne.split(',')] for ligne in contenu.splitlines()]
toutes_distances = []
for i in range(len(liste)):
    for j in range(i + 1, len(liste)):
        d = dist_eucl_3d(liste[i], liste[j])
        toutes_distances.append((d, i, j))

toutes_distances.sort()
circuits = []
nb_points_total = len(liste)

for k in range(1000):
    dist, i, j = toutes_distances[k]

    c_i = next((s for s in circuits if i in s), None)
    c_j = next((s for s in circuits if j in s), None)

    if c_i is None and c_j is None:
        circuits.append({i, j})
    elif c_i is not None and c_j is None:
        c_i.add(j)
    elif c_j is not None and c_i is None:
        c_j.add(i)
    elif c_i != c_j:
        c_i.update(c_j)
        circuits.remove(c_j)

tailles = [len(c) for c in circuits]

points_connectes = sum(tailles)
nb_points_isoles = nb_points_total - points_connectes
for _ in range(nb_points_isoles):
    tailles.append(1)

tailles.sort(reverse=True)

print(f"Tailles de tous les circuits : {tailles}")
print(f"Nombre total de circuits : {len(tailles)}")
print(f"Nombre total de junction boxes : {sum(tailles)}")

if len(tailles) >= 3:
    score = tailles[0] * tailles[1] * tailles[2]
    print(f"Résultat : {score}") # 24360
        

circuits = [{i} for i in range(len(liste))]
last_pair = (None, None)
for dist, i, j in toutes_distances:
    c_i = next(s for s in circuits if i in s)
    c_j = next(s for s in circuits if j in s)

    if c_i != c_j:
        last_pair = (i, j)
        c_i.update(c_j)
        circuits.remove(c_j)
        if len(circuits) == 1:
            break

p1_idx, p2_idx = last_pair
x1 = liste[p1_idx][0]
x2 = liste[p2_idx][0]

resultat = x1 * x2

print(f"Dernière connexion entre le point {p1_idx} et {p2_idx}")
print(f"Coordonnées X : {x1} et {x2}")
print(f"Résultat final : {resultat}") # 2185817796