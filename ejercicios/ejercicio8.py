# Escribí un programa que solicite al usuario el ingreso de dos números diferentes y muestre en pantalla al mayor de los dos.
# Y si son iguales tambien mostrar por pantalla que son iguales.

numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

if numero1 > numero2:
    print(f"El número mayor es el: {numero1}")
elif numero1 < numero2:
    print(f"El número mayor es el: {numero2}")
else:
    print("Los números ingresados son iguales")