numeros = list(map(int, input().split()))

lideres = []

for i in range(len(numeros)):
    if numeros[i] > max(numeros[i+1:], default=-1):
        lideres.append(numeros[i])

print(*lideres)

