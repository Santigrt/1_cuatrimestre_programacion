lista_numeros = [56, 54, 76, 34]

lista_flotantes = [34.5, 56.7, 78.9]

lista_nombres = ["Juan", "Maria", "Pedro"]


print(lista_nombres[0]) # Juan
print(lista_nombres[1]) # Maria


# Allocated ---> populated

lista = [None] * 5 # [None, None, None, None, None]

for i in range(len(lista)):
    lista[i] = i

print(lista) # [0, 1, 2, 3, 4]

for i in range(len(lista)):
    print(lista[i], end=" ") # 0 1 2 3 4