'''
Clase:        fundamentos de la programacion
Tema:         variables,tipos,entradas y salidas
Ejercicio:   generador correo de key 
descripcion:Solicita al usuario su nombre completo (asume dos nombres y
dos apellidos). Luego, el programa generará, su correo con el
formato:
• primer_nombre.primer_apellido@keyinstitute.edu.sv

Autor:        Jose Andres Aviles Torres
Fecha:        2025-05-12
Estado:       [ Terminado ]
'''

# Generador de correo simple
persona=input("Ingresa tu nombre completo: ")

partes=persona.split()  # separa las palabras y las guarda en una lista

usuario=partes[0].lower()
apellido_final=partes[2].lower()

print("Tu correo asignado es: "+usuario+"."+apellido_final+"@keyinstitute.edu.sv")
