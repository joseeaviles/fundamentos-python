'''
Clase:        Clase 11
Tema:         Introducción a NumPy 
Ejercicio:   Diagonal principal y secundaria
Descripción: 

Autor:        Jose Andres Aviles Torres 
Fecha:        2025-06-11
Estado:       [ Terminado ]
'''

jose = 4

hola = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

diagonal_principal = []
diagonal_secundaria = []

for fila in range(jose):
    diagonal_principal.append(hola[fila][fila])
    diagonal_secundaria.append(hola[fila][jose - 1 - fila])

print(diagonal_principal)
print(diagonal_secundaria)
