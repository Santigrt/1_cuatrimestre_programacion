# WHILE VALIDACIONES

#1)
'''CLAVE = "python123"
ingreso_clave = input("Ingrese la clave: ")

while ingreso_clave != CLAVE:
    print("Clave incorrecta. Intente nuevamente.")
    ingreso_clave = input("Ingrese la clave: ")
'''
#2)
'''CLAVE = "python123"
ingreso_clave = input("Ingrese la clave: ")
intentos = 0

while intentos < 2:
    if ingreso_clave != CLAVE:
        print("Clave incorrecta. Intente nuevamente.")
        ingreso_clave = input("Ingrese la clave: ")
    intentos += 1

if intentos == 3:
    print("Te quedaste sin intentos")
else:
    print("Ingreso valido.")'''

#3)
'''nota = int(input("Ingrese la nota: "))

while nota < 1 or nota > 10:
    print("Nota invalida, ingrese una nota del 1 al 10.")
    nota = int(input("Ingrese la nota: "))
print("Nota valida")'''

#4)
'''color = input("Ingrese un color: ")

while color != 'rojo' and color != 'verde' and color != 'azul':
    print("Color incorrecto")
    color = input("Ingrese nuevamente el color: ")
print(f"Color {color} ingresado correctamente.")'''

# INTEGRADOR WHILE

'''apellido = input("Ingrese el apellido: ")

edad = int(input("Ingrese la edad: "))

while edad < 18 or edad > 90:
    edad = int(input("Error. Edad no valida. \nIngrese la edad (18 a 90): "))

estado_civil = input("Estado civil: “Soltero/a”, ”Casado/a”, “Divorciado/a” o “Viudo/a”: ")

condicion = (estado_civil != "Soltero" and estado_civil != "Soltera" and 
        estado_civil != "Casado" and estado_civil != "Casada" and 
        estado_civil != "Divorciado" and estado_civil != "Divorciada" and 
        estado_civil != "Viudo" and estado_civil != "Viuda")

while condicion:
    estado_civil = input("Error. \nIngrese el Estado civil: “Soltero/a”, ”Casado/a”, “Divorciado/a” o “Viudo/a”: ")

legajo = int(input("Numero de legajo: "))

while legajo < 1000 or legajo > 9999:
    legajo = int(input("\nError. El legajo debe tener 4 cifras y no empezar con 0. Reingrese: "))

print(f"\nSu apellido es: {apellido}")
print(f"Su edad es: {edad}")
print(f"Su estado civil es: {estado_civil}")
print(f"Su numero de legajo es: {legajo}")
print(f"\nGracias por utilizar nuestra empresa!")'''

# Pedir hora al usuario (0 a 23). 
# 6 a 11 -> Buenos días
# 12 a 19 -> Buenas tardes
# Caso contrario -> Buenas noches

hora = int(input("ingrese la hora (0 - 23): "))

while hora < 0 or hora > 23:
    hora = int(input("Error, ingrese la hora (0 - 23): "))

if hora >= 6 and hora <= 11:
    print("Buenos dias!!")
elif hora >= 12 and hora <= 19:
    print("Buenas tardes!!")
else:
    print("Buenas noches!!!")