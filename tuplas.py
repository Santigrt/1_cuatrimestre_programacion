variable = (23, 43, 12, 54, 34)

for i in range(len(variable)):
    print(variable[i])

tupla_un_valor = (23,)

print(type(tupla_un_valor))
paises = ("Argentina", "Bolivia", ("Hola", 67, 87), "Chile", "Paraguay", "Peru", "Uruguay")

print(paises[-1])
tupla_de_dias = ("Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo")
print(tupla_de_dias)
print(id(tupla_de_dias))

tupla_de_dias = ("Lunes", "Martes", "Miercoles", "Jueves", "Viernes")
print(tupla_de_dias)
print(id(tupla_de_dias))
tupla = ("Lautaro", "Vallejos", 20, 2)


nombre, apellido, edad, nota = tupla

print(nombre)
print(apellido)
print(edad)
print(nota)


configuracion_bd = ('localhost', 5432, 'mi_base_de_datos', 'admin', 'admin123')


host, puerto, nombre_bd, usuario, password = configuracion_bd