'''
Clase:        fundamentos de la programacion
Tema:         Bloques condicionales
Ejercicio:     Cálculo de impuesto
Descripcion: Desarrollar un programa en Python que permita calcular el impuesto que debe pagar
un usuario por el consumo de energía. El cálculo debe realizarse basado en la siguiente
tabla

Autor:        Jose Andres Aviles Torres
Fecha:        2025-05-14
Estado:       [ Terminado ]
'''


# Cálculo de tarifa de consumo

uso=int(input("Cantidad de unidades usadas: "))

if uso <= 100:
    print("Total sin impuesto:", uso)

if uso > 100 and uso <= 200:
    print("El impuesto es: $"+str(uso*0.5))

if uso > 200:
    print("El impuesto es: $"+str(uso*0.7))

