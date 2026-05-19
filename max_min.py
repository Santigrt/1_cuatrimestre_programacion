#MINIMO
cantidad = 5
minimo = 999999999999999


for i in range(cantidad):
    numero = int(input(f"Ingrese un numero entero, vuelta numero {i + 1}: "))
    if numero < minimo:
        minimo = numero

print(f"El numero minimo es: {minimo}")

#MINIMO CON WHILE

cantidad = int(input("Ingrese la cantidad de numeros a ingresar: "))
contador = 0
minimo = float("inf")

while contador < cantidad:
    numero = int(input(f"Ingrese un numero entero, vuelta numero {contador + 1}: "))
    if numero < minimo:
        minimo = numero
    contador += 1

#MAXIMO
cantidad = 5
maximo = float("-inf")

for i in range(cantidad):
    numero = int(input(f"Ingrese un numero entero, vuelta numero {i + 1}: "))
    if numero > maximo:
        maximo = numero

print(f"El numero maximo es: {maximo}")

















cantidad = int(input("Ingrese la cantidad: "))
minimo = float("inf")
maximo = float("-inf")

for i in range(cantidad):
    numero = int(input(f"Ingrese un numero entero, vuelta numero {i + 1}: "))
    if numero > maximo:
        maximo = numero
        