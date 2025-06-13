'''
Clase:        Clase 11
Tema:         Introducción a NumPy 
Ejercicio:     Matriz simétrica
Descripción:  

Autor:        Jose Andres Aviles Torres 
Fecha:        2025-06-11
Estado:       [ Terminado ]
'''

jose = 3

hola = [
    [1, 2, 3],
    [2, 5, 0],
    [3, 0, 5]
]

es_simetrica = True

for fila in range(jose):
    for col in range(jose):
        if hola[fila][col] != hola[col][fila]:
            es_simetrica = False

if es_simetrica:
    print("La matriz es simétrica")
else:
    print("La matriz no es simétrica")
