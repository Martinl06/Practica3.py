
dicc = {
    "nombre":"Miguel",
    "edad": "30",
    "apellido":"Sanchez"
}

consulta = input("Escriba su consulta: ")

def consultas():
    try:
        resultado = dicc[consulta]
        print(f"Su consulta es: {resultado}")
    except KeyError:
        print("Su consulta no esta en la base de datos")

consultas()