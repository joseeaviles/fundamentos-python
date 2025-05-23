'''
Clase:        fundamentos de la programacion
Tema:        bloque condicional
Ejercicio:   Contraseña segura
descripcion: Solicita una cadena de texto que representa una contraseña, y verifica si la contraseña
cumple con las siguientes condiciones: tener al menos 8 caracteres, un número y una
mayúscula
Fecha:        2025-05-14
Estado:       [ Terminado ]
'''


# Verificar seguridad de clave

clave=input("Escribe tu clave: ")

tiene_mayus=False
tiene_numero=False

for letra in clave:
    if letra.isupper():
        tiene_mayus=True
    if letra.isdigit():
        tiene_numero=True

if tiene_mayus==True and tiene_numero==True and len(clave)>=8:
    print("Clave aceptada")
else:
    print("Clave débil")
