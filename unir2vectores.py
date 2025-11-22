#ID: 1476 Unir dos vectores (Juez Patito)
# Leer N y M
n, m = map(int, input().split())


a = list(map(int, input().split()))

# Leer vector B  
b = list(map(int, input().split()))

# Unir los dos vectores
c = a + b

# Ordenar de menor a mayor
c.sort()

# Imprimir un elemento por línea
for num in c:
    print(num)

print("emma clara lazo layme")