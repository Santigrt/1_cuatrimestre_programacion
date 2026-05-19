# iterativa vs recursiva
#def contar_iterativo(numero):
#    for i in range(numero, -1, -1):
#        print(i)
#
#contar_iterativo(5)


#def contar_recursiva(numero):
#    if numero < 0:
#        return
#    contar_recursiva(numero - 1)
#    print(numero)
#
#contar_recursiva(5)

#def factorial_iterativo(numero):
#    if numero < 0:
#        return -1
#    elif numero == 0:
#        return 1
#    else:
#        for i in range(1, numero):
#            numero *= i
#    return numero
#
#
#print(factorial_iterativo(5))

#def factorial_recursiva(numero):
#    if numero == 0:
#        return 1
#    else:
#        return numero * factorial_recursiva(numero - 1)
#
#print(factorial_recursiva(5))

def fibonacci(numero):
    if numero == 0:
        return 0
    if numero == 1:
        return 1
    else:
        return fibonacci(numero - 1) + fibonacci(numero - 2)

print(fibonacci(6))