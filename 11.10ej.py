# Leer los números
numeros = input().split()
vector = []
for num in numeros:
    vector.append(int(num))

# Contar cuántas veces aparece cada número
contador = {}
for num in vector:
    if num in contador:
        contador[num] += 1
    else:
        contador[num] = 1

# Encontrar la mayor repetición
max_repeticiones = 0
for num in contador:
    if contador[num] > max_repeticiones:
        max_repeticiones = contador[num]

# Mostrar los números que más se repiten
print("Números que más se repiten:")
for num in contador:
    if contador[num] == max_repeticiones:
        print(num)