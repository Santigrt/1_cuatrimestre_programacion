# Para pagar un determinado impuesto se debe ser mayor de 18 años y tener unos 
# ingresos iguales o superiores a 20.000 ARS mensuales. Escribir un programa que pregunte 
# al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que pagar un impuesto o no.

edad = int(input("Por favor, ingresa tu edad: "))
MONTO_INGRESO = 20000

if edad > 0:
    if edad >= 18:
        ingresos_mensuales = float(input("Coloca tus ingresos mensuales: "))
        if ingresos_mensuales >= MONTO_INGRESO:
            print("Debes pagar el impuesto.")
        else:
            print("No pagas el impuesto porque el ingreso mensual debe ser superior a $20.000")
    else:
        print("No pagas el impuesto por que eres menor de edad.")
else:
    print("Ingrese una edad valida.")




# otra forma
edad = int(input("Por favor, ingresa tu edad: "))
ingresos_mensuales = float(input("Coloca tus ingresos mensuales: "))