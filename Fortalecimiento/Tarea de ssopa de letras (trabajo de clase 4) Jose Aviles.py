lineas = []
palabras_e = ["PAJARO", "GATO", "GATOS", "TIGRE", "PERRO", "RATON"]
with open("sopa_de_letras.txt", "r") as f:
    for linea in f:
        print(linea)
        a = linea.strip().split()
        lineas.append(a)

print(lineas)
counter = 0 
for fila in lineas:
    texto = "".join(fila)
    for palabra in palabras_e:
        y = texto.find(palabra)
        if palabra in texto:
            print (f"{palabra} [{counter}, {y}]")
    counter +=1
