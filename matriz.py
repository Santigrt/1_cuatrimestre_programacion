matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

def mostrar_matriz_for(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end=" ")
        print()

def mostrar_matriz_while(matriz):
    i = 0
    while i < len(matriz):
        j = 0
        while j < len(matriz[i]):
            print(matriz[i][j], end=" ")
            j += 1
        i += 1
        print()

