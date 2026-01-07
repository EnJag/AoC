def aire_rectangle(pos1,pos2):
    x1, x2, y1, y2 = pos1[0], pos2[0], pos1[1], pos2[1]
    return (abs(x2-x1)+1)*(abs(y2-y1)+1)
with open('f9/f9.txt') as fichier:
    contenu=fichier.read()
positions=[(int(el.split(',')[0]),int(el.split(',')[1])) for el in contenu.splitlines()]
# print(positions)
aires = []
for i in range(len(positions)):
    for j in range(i+1,len(positions)):
        aires.append((aire_rectangle(positions[i],positions[j]), positions[i], positions[j]))
print(sorted(aires)[-1][0]) # 4737096935


def is_inside(x, y, segments_v):
    count = 0
    for sx, sy_min, sy_max in segments_v:
        if sx > x and sy_min <= y < sy_max:
            count += 1
    return count % 2 == 1
 
segments_v = []
segments_h = []
for i in range(len(positions)):
    p1 = positions[i]
    p2 = positions[(i + 1) % len(positions)]
    if p1[0] == p2[0]: # Vertical
        segments_v.append((p1[0], min(p1[1], p2[1]), max(p1[1], p2[1])))
    else: # Horizontal
        segments_h.append((p1[1], min(p1[0], p2[0]), max(p1[1], p2[0])))

max_area = 0
n = len(positions)

for i in range(n):
    for j in range(i + 1, n):
        p1, p2 = positions[i], positions[j]
        x_min, x_max = min(p1[0], p2[0]), max(p1[0], p2[0])
        y_min, y_max = min(p1[1], p2[1]), max(p1[1], p2[1])
        
        area = (x_max - x_min + 1) * (y_max - y_min + 1)
        if area <= max_area:
            continue

        possible = True
        for sx, sy_min, sy_max in segments_v:
            if x_min < sx < x_max and not (sy_max <= y_min or sy_min >= y_max):
                possible = False; break
        if not possible: continue
        
        for sy, sx_min, sx_max in segments_h:
            if y_min < sy < y_max and not (sx_max <= x_min or sx_min >= x_max):
                possible = False; break
        if not possible: continue

        if is_inside((x_min + x_max) / 2, (y_min + y_max) / 2, segments_v):
            max_area = area
print(max_area)            
