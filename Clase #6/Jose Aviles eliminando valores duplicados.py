numeros = list(map(int, input().split()))

vistos = []
for num in numeros:
    if num not in vistos:
        vistos.append(num)

print(*vistos)