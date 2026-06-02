'''
Ejercicio 1
Crea un programa que encuentre la/las posición(es) del valor más grande en una matriz de enteros.
Restricciones :
No uses listas por comprensión, métodos de listas (como .max()), ni funciones integradas salvo len() y range().
Usa únicamente bucles for y comparaciones directas.
'''

matriz = [
    [1, 3, 2],
    [65, 9, 4],
    [7, 65, 8]
]

#sin append
def encontrar_posiciones_maximo(matriz):
    mas_alto = matriz[0][0]
    posiciones = [[0, 0]]
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] > mas_alto:
                mas_alto = matriz[i][j]
                posiciones = [[i, j]]
            elif matriz[i][j] == mas_alto:
                if [i, j] != [0, 0]:
                    posiciones += [[i, j]]
    return posiciones

posiciones_maximo = encontrar_posiciones_maximo(matriz)
print("Posiciones del valor más grande:", posiciones_maximo)