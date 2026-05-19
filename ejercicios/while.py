#numero = 1
#
#while numero <= 10:
#    print(numero)
#    numero += 1
#
#numero = 10
#
#while numero >= 1:
#    print(numero)
#    numero -= 1
#
#
#acumulador = 0
#contador = 0
#while contador <= 10:
#    acumulador += contador
#    contador += 1
#
#print(f"La suma de los numeros del 0 al 10 es: {acumulador}")

#suma = 0
#contador = 0
#
#
#while contador <= 10:
#    if contador % 2 == 0:
#        suma += contador
#    contador += 1
#
#print(f"La suma de los numeros pares del 0 al 10 es: {suma}")
#
##con for
#suma = 0
#for i in range(1, 11):
#    if i % 2 == 0:
#        suma += i
#
#print(f"La suma de los numeros pares del 0 al 10 es: {suma}")

#contador = 0
#suma = 0
#
#while contador < 5:
#    numero = int(input(f"Ingrese el numero {contador + 1}: "))
#    suma += numero
#    contador += 1
#
#promedio = suma / contador
#print(f"La suma de los numeros ingresados es: {suma}")
#print(f"El promedio de los numeros ingresados es: {promedio}")


# Solicitar al usuario que ingrese 5 numeros como minimo y como maximos 10.
# Calcular la suma de los numeros ingresados y el promedio de los mismos.

contador = int(input("Ingrese la cantidad de numeros a ingresar: "))
while contador < 5 or contador > 10:
    contador = int(input("Ingrese la cantidad de numeros a ingresar de 5 a 10: "))
