# sintaxis
numero = int(input("Ingrese un numero entre 1 y 3: "))

match numero:
    case 1:
        print("El numero es 1.")
    case 2:
        print("El numero es 2.")
    case 3:
        print("El numero es 3.")
    case _:
        print("El numero no esta entre 1 y 3.")

##################################################

# Patrones Literales
# Se comparan valores simples, similares a una sentencia if

# Ejemplo 1: Manejo de strings (comandos)
comando = "start"

match comando:
    case "iniciar":
        print("Sistema iniciado")
    case "detener":
        print("Sistema detenido")
    case "ayuda":
        print("Mostrando ayuda...")
    case _:
        print("Comando no reconocido")

# Ejemplo 2: Manejo de enteros (numeros)
numero = 10

match numero:
    case 0:
        print("El numero es 0")
    case 1:
        print("El numero es 1")
    case 2:
        print("El numero es 2")
    case _:
        print("El numero no es 0, 1 o 2")

# Ejemplo 3: Manejo de floats (decimales)
numero = 10.5

match numero:
    case 0.0:
        print("El numero es 0.0")
    case 1.0:
        print("El numero es 1.0")
    case 2.0:
        print("El numero es 2.0")
    case _:
        print("El numero no es 0.0, 1.0 o 2.0")

##################################################

# Patrones or (operador |)
numero = int(input("Ingrese un numero entre 1 y 6: "))

match numero:
    case 1 | 2: # Esta línea indica que si numero es 1 o 2, se ejecuta esa instrucción.
        print("El numero es 1 o 2.")
    case 3 | 4:
        print("El numero es 3 o 4.")
    case 5 | 6:
        print("El numero es 5 o 6.")
    case _:
        print("El numero no esta entre 1 y 6.")

# - El símbolo | funciona como un "o" lógico: equivale a numero == 1 or numero == 2.
# - El código permite agrupar varios valores posibles en un mismo case usando |.
# - La sintaxis es más legible que usar muchos if o elif.
# - Es más expresiva y moderna, útil especialmente si vas a trabajar con estructuras más complejas.


# Mismo código, pero usando if, elif y else en lugar de match
numero = int(input("Ingrese un numero entre 1 y 6: "))

if numero == 1 or numero == 2:
    print("El numero es 1 o 2.")
elif numero == 3 or numero == 4:
    print("El numero es 3 o 4.")
elif numero == 5 or numero == 6:
    print("El numero es 5 o 6.")
else:
    print("El numero no esta entre 1 y 6.")

##################################################


# Para manejar diferentes tipos de datos, se puede utilizar la función type() en la expresión de match
dato = "Python"

match dato:
    case str():
        print(f"Recibido texto: {dato}")
    case int() | float():
        print(f"Recibido número: {dato}")
    case list():
        print(f"Recibida lista con {len(dato)} elementos")
    case _:
        print("Tipo no soportado")

##################################################

# Manejo de rangos. Patrones con Guardias (if)
# Se pueden agregar condiciones adicionales usando if al final de la línea de un case

# Manejo de enteros con rangos
numero = 7

match numero:
    case n if n < 0:
        print("Número negativo")
    case 0:
        print("Cero")
    case 1 | 2 | 3:
        print("Número pequeño")
    case n if 4 <= n <= 10:
        print("Número mediano")
    case _:
        print("Número grande")


# Manejo de floats con rangos
temperatura = 75.0

match temperatura:
    case t if t < 0.0:
        print("Estado sólido")
    case 0.0 | 100.0:
        print("Punto de cambio de estado")
    case t if 0.0 < t < 100.0:
        print("Estado líquido")
    case _:
        print("Estado gaseoso")


# explicacion del ejemplo con enteros
# 1. match numero:
#   - Se evalúa la variable numero (que vale 7 en este caso) contra cada uno de los patterns en los bloques case.
# 2. case n if n < 0:
#   - n: Es una variable que actúa como pattern variable. Esto significa que este case "captura" el valor de numero y lo asigna a n.
#   - if n < 0: Es una guard clause (condicional adicional) que impone una condición extra. El case solo se ejecutará si, además de 
#   coincidir el patrón (que en este caso siempre coincide al capturar el valor), la condición n < 0 es verdadera.
#   En resumen: Aunque la variable n recibe el valor de numero, la ejecución del bloque sólo ocurrirá si n es negativo.
# 3. Otros casos:
#   - case 0: Se ejecuta si numero es igual a 0.
#   - case 1 | 2 | 3: Se ejecuta si numero es 1, 2 o 3.
#   - case n if 4 <= n <= 10: De manera similar al primer caso, captura el valor en n y luego lo evalúa con la condición. Se ejecuta si numero es mayor o igual a 4 y menor o igual a 10.
#   - case _: Es el wildcard, se ejecuta para cualquier otro valor que no haya cumplido con los casos anteriores.

##################################################

# Explicación detallada de "patrones con guardia":
# el término "patrón con guardia" se refiere a la combinación de un patrón en una estructura de control, 
# como match-case en Python, con una condición adicional que debe cumplirse para que el bloque correspondiente 
# se ejecute. Esta condición adicional se denomina "guardia" y se especifica utilizando la cláusula if después 
# del patrón. La razón por la que se llaman "patrones con guardia" es precisamente porque incorporan esta 
# condición (if) que actúa como una salvaguarda o filtro adicional para determinar si el bloque de código debe ejecutarse.

# En el contexto de match-case en Python, un patrón con guardia permite que, incluso si un valor coincide 
# con el patrón especificado, el bloque de código asociado solo se ejecute si la expresión booleana de la 
# guardia evalúa a True. Esto proporciona un control más preciso sobre el flujo del programa. 

##################################################





##################################################
# NO SON NECESARIOS CONOCERLOS PARA LA CURSADA
# NO SON NECESARIOS CONOCERLOS PARA LA CURSADA
# NO SON NECESARIOS CONOCERLOS PARA LA CURSADA
# Patrones compuestos
# Se comparan valores complejos, similares a una sentencia if-elif-else

# Ejemplo 1: Manejo de tuplas
tupla = (1, 2, 3)

match tupla:
    case (1, 2, 3):
        print("La tupla es (1, 2, 3)")
    case (4, 5, 6):
        print("La tupla es (4, 5, 6)")
    case _:
        print("La tupla no es (1, 2, 3) ni (4, 5, 6)")

# Ejemplo de tuplas
punto = (0, 4)

match punto:
    case (0, 0):
        print("El punto está en el origen.")
    case (0, y):
        print(f"El punto está sobre el eje Y en y={y}.")
    case (x, 0):
        print(f"El punto está sobre el eje X en x={x}.")
    case (x, y):
        print(f"El punto está en la posición x={x}, y={y}.")
    case _:
        print("No es un punto válido.")


# Ejemplo 2: Manejo de listas
lista = [1, 2, 3]

match lista:
    case [1, 2, 3]:
        print("La lista es [1, 2, 3]")
    case [4, 5, 6]:
        print("La lista es [4, 5, 6]")
    case _:
        print("La lista no es [1, 2, 3] ni [4, 5, 6]")


# Ejemplo 3: Manejo de diccionarios
diccionario = {"a": 1, "b": 2, "c": 3}

match diccionario:
    case {"a": 1, "b": 2, "c": 3}:
        print("El diccionario es {'a': 1, 'b': 2, 'c': 3}")
    case {"d": 4, "e": 5, "f": 6}:
        print("El diccionario es {'d': 4, 'e': 5, 'f': 6}")
    case _:
        print("El diccionario no es {'a': 1, 'b': 2, 'c': 3} ni {'d': 4, 'e': 5, 'f': 6}")


# Ejemplo 4: Manejo de conjuntos
# El match case en Python tiene limitaciones específicas al trabajar con conjuntos (set)
conjunto = {1, 2, 3}
# El error ocurre porque Python interpreta los patrones {1, 2, 3} en los case como diccionarios, no como conjuntos.
# Los conjuntos no son directamente compatibles en los patrones de match case, y esta sintaxis genera un error de sintaxis 
""" match conjunto:
    case {1, 2, 3}:
        print("El conjunto es {1, 2, 3}")
    case {4, 5, 6}:
        print("El conjunto es {4, 5, 6}")
    case _:
        print("El conjunto no es {1, 2, 3} ni {4, 5, 6}") """


conjunto = {1, 2, 3}
# El match case en Python no puede comparar conjuntos directamente pero se puede usar un patrón compuesto
# con un operador as para acceder al conjunto dentro del patrón
match conjunto:
    case set() as s if s == {1, 2, 3}:
        print("El conjunto es {1, 2, 3}")
    case set() as s if s == {4, 5, 6}:
        print("El conjunto es {4, 5, 6}")
    case _:
        print("El conjunto no es {1, 2, 3} ni {4, 5, 6}")

##################################################

# Ejemplos de tuplas
# Los patrones de tuplas permiten comparar y desestructurar tuplas, 
# facilitando el acceso a sus elementos de forma clara. A continuación, 
# se presenta un ejemplo que determina la ubicación de un punto en un plano cartesiano:
punto = (0, 4)

match punto:
    case (0, 0):
        print("El punto está en el origen.")
    case (0, y):
        print(f"El punto está sobre el eje Y en y={y}.")
    case (x, 0):
        print(f"El punto está sobre el eje X en x={x}.")
    case (x, y):
        print(f"El punto está en la posición x={x}, y={y}.")
    case _:
        print("No es un punto válido.")


# Ejemplos de listas
# Los patrones de listas permiten desestructurar listas y acceder a sus elementos. 
# Por ejemplo, para interpretar comandos representados como listas de cadenas:
comando = ["ir", "norte"]

match comando:
    case ["ir", direccion]:
        print(f"Moviéndose hacia el {direccion}.")
    case ["salir"]:
        print("Saliendo del programa.")
    case _:
        print("Comando no reconocido.")


# Uso de * para Capturar Elementos Restantes
# Al igual que en la asignación de variables, se puede usar el 
# operador * para capturar múltiples elementos en una lista o tupla:
valores = [1, 2, 3, 4, 5]

match valores:
    case [primero, segundo, *resto]:
        print(f"Primer valor: {primero}")
        print(f"Segundo valor: {segundo}")
        print(f"Valores restantes: {resto}")
    case _:
        print("Lista vacía o con menos de dos elementos.")

# NO SON NECESARIOS CONOCERLOS PARA LA CURSADA
# NO SON NECESARIOS CONOCERLOS PARA LA CURSADA
# NO SON NECESARIOS CONOCERLOS PARA LA CURSADA
##################################################