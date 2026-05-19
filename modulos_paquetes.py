# Primero Librerias estandar de python
#from math import floor, ceil, sqrt
#import os

# Segundo Librerias de terceros
#import pandas

# Tercero Librerias propias
import aritmeticas

opcion = int(input("Ingrese una opcion: 1 | Sumar, 2 | Restar, 3 | Multiplicar, 4 | Dividir: "))
numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))

match opcion:
    case 1:
        print(aritmeticas.sumar(numero1, numero2))
    case 2:
        print(aritmeticas.restar(numero1, numero2))
    case 3:
        print(aritmeticas.multiplicar(numero1, numero2))
    case 4:
        print(aritmeticas.dividir(numero1, numero2))

print(aritmeticas.PI)