#conjunto = {1, 2, 3, 4, 5, 6, "Python", 6.76, (54, 32)}
#print(conjunto)

#conjunto = set([23, 43, 12, 54, 34])
#print(conjunto)

#conjunto = set()
#print(type(conjunto))

#conjunto = {77, "Ataque", "Python", 32, True}
#print(conjunto)

#conjunto_1 = {1, 5, 76, 45, 2, 43, 3}
#conjunto_2 = {5, 2, 3}

#print(conjunto_1 > conjunto_2)

#conjunto = list({1, 5, 76, 45, 2, 43, 3})

#for i in range(len(conjunto)):
#    print(conjunto[i])

#conjunto_letras = {"a", "b", "c", "d", "e"}

#lista_letras = list(conjunto_letras)

#for i in range(len(lista_letras)):
#    print(lista_letras[i])

#conjunto = {1, 5, 76, 45, 2, 43, 3}

#foreach
#for i in conjunto:
#    print(i)

#Metodos de conjuntos

#numeros = {1, 2, 3, 4, 5}
#print(numeros)
#print(id(numeros))

#numeros.add(6)
#print(numeros)
#
#numeros.clear()
#print(numeros)
#
#numeros_copia = numeros.copy()
#print(numeros_copia)
#print(id(numeros_copia))
#
#numeros.add(7)
#
#print(numeros)
#print(numeros_copia)

#conjunto = {"a", "b", "c", "d", "e"}

#eliminado = conjunto.pop()
#print(conjunto)
#print(eliminado)
#
#conjunto.update({5, 79, 685})
#print(conjunto)

#conjunto.remove("c")
#print(conjunto)
#
#conjunto.discard(777)
#print(conjunto)



set1 = {1, 2, 3, 7, 8, 9}
set2 = {1, 2, 3, 4, 5, 6}

print(set1.isdisjoint(set2))

print(set1.issubset(set2))

print(set2.issuperset(set1))

print(set1.union(set2))

print(set1.intersection(set2))

print(set1.difference(set2))