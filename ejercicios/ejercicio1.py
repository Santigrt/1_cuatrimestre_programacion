# Escribir un programa que almacene la cadena de caracteres prog1Div115 en una variable, 
# pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida 
# por el usuario coincide con la guardada en la variable

contrasena_guardada = "python"
contrasena = input("Ingrese su contraseña")

if contrasena == contrasena_guardada:
    print("Contraseña ingresada correctamente.")
else:
    print("Contraseña incorrecta.")



# con match
match contrasena:
    case str(contrasena_guardada):
        print("Contraseña ingresada correctamente.")
    case _:
        print("Contraseña incorrecta.")