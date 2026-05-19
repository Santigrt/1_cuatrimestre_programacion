'''def saludar(): # Cabezera de la funcion
    saludo = "Estoy saludando desde la funcion" # Cuerpo de la funcion
    print(saludo)

# llamar o invocar
saludar()'

def saludar_con_nombre(nombre): 
    print(f"Hola {nombre}, como andas?")

saludar_con_nombre("Juan")

def saludar_con_nombre_y_edad(nombre, edad): # Parametros formales
    print(f"Hola {nombre}, como andas? Tenes {edad} años")

usuario = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
saludar_con_nombre_y_edad(usuario, edad) # Parametros actuales o argumentos



def sumar(num1, num2):
    resultado = num1 + num2
    return resultado

variable = sumar(5, 3)
print(variable)

def solicitar_datos():
    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad: "))
    return nombre, edad

nombre, edad = solicitar_datos() # Desempaquetado
print(f"Hola {nombre}, tenes {edad} años")

def restar(num1, num2):
    resultado = num1 - num2
    return resultado

print(restar(num2=10, num1=5)) # parametros nombrados, no importa el orden

def restar(num1=0, num2=0):
    return num1 - num2

resultado = restar(10, 5)
print(resultado)

# sugerencia de tipos / type hints

def sumar(num1: int, num2: int) -> int:
    resultado = num1 + num2
    return resultado

print(sumar(5, 3))

def saludar(nombre: str) -> str:
    resultado = nombre.lower()
    return resultado

variable = saludar("Juan")
print(variable)



def es_par(numero):
    if numero % 2 == 0:
        resultado = f"El numero {numero} es par"
    else:
        resultado = f"El numero {numero} es impar"
    return resultado

numero = int(input("Ingrese un numero: "))
resultado = es_par(numero)
print(resultado)'''


# FUNCION
# Cohesion: una funcion debe realizar una sola tarea, y realizarla bien. Si una funcion hace muchas cosas,
# es dificil de mantener y de entender. Es mejor tener varias funciones pequeñas que hagan una sola cosa, que una funcion grande que haga muchas cosas.

# acoplamiento: una funcion debe ser lo mas independiente posible de otras funciones. Si una funcion depende de muchas otras funciones, 
# es dificil de mantener y de entender. Es mejor tener funciones que no dependan de otras funciones, o que dependan de pocas funciones.


# Documentacion: 
def sumar(num1: int | float, num2: int | float=0) -> int | float:
    '''
    Esta funcion recibe dos numeros enteros y devuelve la suma de ambos numeros.
    
    Args:
        num1: (int | float) El primer numero a sumar.
        num2: (int | float) El segundo numero a sumar. Por defecto es 0.
    Returns:
        (int | float) La suma de ambos numeros.
    '''
    resultado = num1 + num2
    return resultado

sumar(3, 4)

