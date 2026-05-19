# Escribí un programa que solicite al usuario una letra y, si es una vocal, muestre el mensaje “Es vocal”. 
# Verificar si el usuario ingresó un string de más de un carácter y, en ese caso, informarle que no se puede procesar el dato.

letra = input("Ingrese una letra: ")

if len(letra) != 1:
    print("No se puede procesar el dato. Ingrese solo una letra.")
else:
    if (letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U" or
        letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u"):
        print("Es vocal")
    else:
        print("No es vocal")