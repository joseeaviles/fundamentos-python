'''
Clase:        fundamentos de la programacion
Tema:         Bloques condicionales
Ejercicios:     
El número mágico

Crea un programa en Python para determinar si un número es "mágico“.
Un número es “mágico” si es divisible por 7 pero no por 5.

Año bisiesto

Determina si un año es bisiesto, considerando las reglas gregorianas. Para que un año
sea bisiesto, debe cumplir alguna de las siguientes condiciones:
• Si es divisible por 4.
• Si es divisible por 100 y por 400

Autor:        Jose Andres Aviles Torres
Fecha:        2025-05-14
Estado:       [ Terminado ]
'''



# Número especial
numero=int(input("Escribe un número: "))

if numero % 7 == 0 and numero % 5 != 0:
    print("Número especial")
else:
    print("Número común")

# Verificar año
anio=int(input("Ingresa un año: "))

if anio % 4 == 0:
    print("Es bisiesto")
elif anio % 100 == 0 and anio % 400 == 0:
    print("Es bisiesto")
else:
    print("No es bisiesto")
