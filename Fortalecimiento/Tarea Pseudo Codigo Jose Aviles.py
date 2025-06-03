# Paso 1: Definir el contenido de la contraseña. En este caso: "contrasena"
# Paso 2: Definir una variable que contenga todo el abecedario 
# Paso 3: Hacer un for anidado cuyas variables temporales pertenezcan a la variable
# contraseña y a la variable del abecedario respectivamente 
# Paso 4: Recorrer ambas variables para que coincidan los elementos, y cuando lo 
# Paso 5: Añadir a una lista aparte las coincidencias resultantes del loop 
# Paos 6: Mostrar contraseña


import string
password = "contrasena"
ABC = set(string.ascii_letters)
intento = []
intentos = 0
for i in password:
 for j in ABC:
    if j == i:
        intento += j
 
 
 
print(f"La contrasena es {intento}")