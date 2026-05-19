# Escribir un programa que pida al usuario dos números y devuelva su división. Si el usuario introduce el divisor cero debera imprimir un mensaje de error.

primer_numero = float(input("Inrese el primer número: "))
segundo_numero = float(input("Inrese el segundo número: "))

if segundo_numero == 0:
    print("Error. No se puede dividir por cero.")
else:
    division = primer_numero / segundo_numero
    print(f"El resultado de la división es: {division}")