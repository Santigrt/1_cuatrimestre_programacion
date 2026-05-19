#numero = int(input("Ingrese un numero: "))
#
#es_primo = True
#
#if numero < 2:
#    es_primo = False
#else:
#    for i in range(2, numero):
#        if numero % i == 0:
#            es_primo = False
#            break


cantidad = int(input("Ingrese la cantidad de numeros a ingresar: "))
contador = 0
pares = 0

while cantidad < 0:
    cantidad = int(input("Ingrese la cantidad de numeros a ingresar: "))

while contador < cantidad:
    numero = int(input(f"Ingrese un numero entero, vuelta numero {contador + 1}: "))
    if numero % 2 == 0:
        pares += 1
    contador += 1



if cantidad > 0:
    porcentaje = (pares / cantidad) * 100
    print(f"El porcentaje de numeros pares es: {porcentaje:.2f}%")
else:
    print("No se ingresaron numeros.")