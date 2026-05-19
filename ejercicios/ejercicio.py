#primer_numero = int(input("Ingrese el primer número: "))
#segundo_numero = int(input("Ingrese el segundo número: "))
#
#print(primer_numero == segundo_numero)
#print(primer_numero != segundo_numero)
#print(primer_numero > segundo_numero)
#print(primer_numero >= segundo_numero)




#cadena_usuario = input("Introduzca la cadena de texto: ")
#
#resultado = len(cadena_usuario) >= 3 and len(cadena_usuario) < 10
#
#print(resultado)




#numero = 4
#resultado = (numero % 2 == 0) and (numero > 0)
#print(resultado)


temperatura = float(input("Ingrese la temperatura: "))
humedad = float(input("Ingrese la humedad: "))

condicion = (20 <= temperatura <= 25) and (0.7 <= humedad <= 0.9) # version corta

condicion = (temperatura >= 20 and temperatura <= 25) and (humedad >= 0.7 and humedad <= 0.9) # version larga
print(condicion)

