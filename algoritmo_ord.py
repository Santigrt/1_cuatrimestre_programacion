def bubble_sort_ascendente(lista):
    n = len(lista)
    for i in range(n):
        for j in range(n - i - 1):
            if lista[j] > lista[j + 1]:
                temp = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = temp

def bubble_sort_descendente(lista):
    n = len(lista)
    for i in range(n):
        for j in range(n - i - 1):
            if lista[j] < lista[j + 1]:
                temp = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = temp

def insertion_sort_ascendente(lista):
    for i in range(1, len(lista)):
        actual = lista[i]
        j = i - 1
        while (j >= 0) and lista[j] > actual:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = actual

def insertion_sort_descendente(lista):
    for i in range(1, len(lista)):
        actual = lista[i]
        j = i - 1
        while (j >= 0) and lista[j] < actual:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = actual