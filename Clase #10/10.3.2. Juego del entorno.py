'''
Clase:        Clase 11
Tema:         Introducción a NumPy 
Ejercicio:     Juego del entorno
Descripción:  

Autor:        Jose Andres Aviles Torres 
Fecha:        2025-06-11
Estado:       [ Terminado ]
'''

filas = 4
columnas = 5

hola = [
    [1, 0, 1, 1, 1],
    [0, 1, 0, 0, 0],
    [0, 0, 1, 0, 1],
    [1, 1, 0, 0, 0]
]

resultado_jose = []

for f in range(filas):
    fila_nueva = []
    for c in range(columnas):
        conteo = 0
        for mov_f in [-1, 0, 1]:
            for mov_c in [-1, 0, 1]:
                if mov_f == 0 and mov_c == 0:
                    continue
                nueva_f = f + mov_f
                nueva_c = c + mov_c
                if 0 <= nueva_f < filas and 0 <= nueva_c < columnas:
                    conteo += hola[nueva_f][nueva_c]
        fila_nueva.append(conteo)
    resultado_jose.append(fila_nueva)

for fila in resultado_jose:
    print(fila)
