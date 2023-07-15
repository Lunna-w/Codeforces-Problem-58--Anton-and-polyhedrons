n = int(input())

faces = 0

tetrahedron = "Tetrahedron"
cube = "Cube"
octahedron = "Octahedron"
dodecahedron = "Dodecahedron"
icosahedron = "Icosahedron"

for i in range(n):
    polyhedron = input()
    if polyhedron == tetrahedron:
        faces += 4
    elif polyhedron == cube:
        faces += 6
    elif polyhedron == octahedron:
        faces += 8
    elif polyhedron == dodecahedron:
        faces += 12
    elif polyhedron == icosahedron:
        faces += 20

print(faces)