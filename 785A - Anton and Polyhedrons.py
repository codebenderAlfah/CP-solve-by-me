n = int(input())
faces = 0
polyhedrons = []
for i in range(0, n):
    ele = input()
    polyhedrons.append(ele)
for i in polyhedrons:
    if i == "Tetrahedron":
        faces += 4
    elif i == "Cube":
        faces += 6
    elif i == "Octahedron":
        faces += 8
    elif i == "Dodecahedron":
        faces += 12
    elif i == "Icosahedron":
        faces += 20
print(faces)
