# Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.


numero = int(input("Ingrese un número: "))

if numero != 0:
    if numero % 2 == 0:
        print(f"El número {numero} es par")
    else:
        print(f"El número {numero} es impar")
else:
    print(f"El {numero} no es par ni impar")