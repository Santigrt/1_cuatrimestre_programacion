def burbuja_caracteres(texto):
    caracteres = []
    for i in range(len(texto)):
        caracteres += [texto[i]]
    n = len(caracteres)
    print("lista de caracteres: ", caracteres)
    for i in range(n):
        for j in range(n - i - 1):
            if caracteres[j] > caracteres[j + 1]:
                temp = caracteres[j]
                caracteres[j] = caracteres[j + 1]
                caracteres[j + 1] = temp
    print("lista de caracteres ordenada: ", caracteres)
    resultado = ""
    for i in range(len(caracteres)):
        resultado += caracteres[i]
    print("Resultado una vez concatenado de nuevo: ", resultado)
    return resultado




palabra = "8rT!gk"
print(burbuja_caracteres(palabra))