# Leer los números
numeros = input().split()
vector = []
for num in numeros:
    vector.append(int(num))

# Leer las rotaciones
veces = input()
k = int(veces)

# Rotar k veces a la izquierda
for i in range(k):
    primero = vector[0]
    for j in range(len(vector) - 1):
        vector[j] = vector[j + 1]
    vector[len(vector) - 1] = primero

# Mostrar resultado
for num in vector:
    print(num, end=" ")