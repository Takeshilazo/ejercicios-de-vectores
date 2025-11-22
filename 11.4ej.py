#Leer un vector con N n´umeros positivos y mostrar los n´umeros primos que hab´ıa en el vector
#conjuntamente con la posici´on en la que se encontraba.
# Leer el vector
# Leer el vector
# Leer cuántos números
# n# Leer todos los números de una línea

datos = input().split()
vector = [int(x) for x in datos]

# Buscar primos
for i in range(len(vector)):
    num = vector[i]
    if num > 1:
        es_primo = True
        for j in range(2, num):
            if num % j == 0:
                es_primo = False
                break
        if es_primo:
            print(f"Posición {i}: {num}")