# Crea una variable numérica y si esta entre 0 y 10, mostrar un mensaje indicándolo.


numero = float(input("Ingrese un número: "))
    
if 0 <= numero <= 10:
    print("El número está entre 0 y 10.")
else:
    print("El número no está en el rango de 0 a 10.")