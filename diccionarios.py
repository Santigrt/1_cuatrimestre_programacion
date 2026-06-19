#usuario2 = dict([("Nombre", "Carlos"), ("Apellido", "Perez"), ("Edad", 30)]) #No se utiliza pero se puede llegar a ver en algunos casos
#print(usuario2)

usuario = {
    "nombre": "Sara",
    "apellido": "Lopez",
    "edad": 25,
    "materias": {
        "progra1": [8, 7],
        "mate1": [9, 8],
        "arso": [7, 6],
        "ingles": [10, 9],
        "base_datos": {
            "nota1": 8,
            "nota2": 9
        }
    },
}

#print(usuario)
#print(type(usuario))
#
#print(usuario["nombre"])
#print(usuario["apellido"])
#
#print(usuario.get("sueldo", "No existe la clave."))
#
#usuario["nombre"] = "Sofia"
#
print(usuario["materias"]["base_datos"]["nota2"])

usuario["turno"] = "Noche"
print(usuario)
