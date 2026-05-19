def sumar(num1: int | float, num2: int | float) -> int | float:
    '''
    Esta funcion recibe dos numeros enteros y devuelve la suma de ambos numeros.
    
    Args:
        num1: (int | float) El primer numero a sumar.
        num2: (int | float) El segundo numero a sumar.
    Returns:
        (int | float) La suma de ambos numeros.
    '''
    return num1 + num2

def restar(num1: int | float, num2: int | float) -> int | float:
    '''
    Esta funcion recibe dos numeros enteros y devuelve la resta de ambos numeros.
    
    Args:
        num1: (int | float) El primer numero a restar.
        num2: (int | float) El segundo numero a restar.
    Returns:
        (int | float) La resta de ambos numeros.
    '''
    return num1 - num2

def multiplicar(num1: int | float, num2: int | float) -> int | float:
    '''
    Esta funcion recibe dos numeros enteros y devuelve la multiplicacion de ambos numeros.
    
    Args:
        num1: (int | float) El primer numero a multiplicar.
        num2: (int | float) El segundo numero a multiplicar.
    Returns:
        (int | float) La multiplicacion de ambos numeros.
    '''
    return num1 * num2

def dividir(num1: int | float, num2: int | float) -> int | float:
    '''
    Esta funcion recibe dos numeros enteros y devuelve la division de ambos numeros.
    
    Args:
        num1: (int | float) El primer numero a dividir.
        num2: (int | float) El segundo numero a dividir.
    Returns:
        (int | float) La division de ambos numeros.
    '''
    if num2 == 0:
        resultado = "Error: No se puede dividir por cero."
    else:
        resultado = num1 / num2
    return resultado

PI = 3.1416