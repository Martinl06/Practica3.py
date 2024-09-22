
dicc = {
    "Nombre":"Miguel",
    "Edad": "30",
    "Apellido":"Sanchez"
}

consulta = input("Escriba su consulta: ")

def consultas():
    try:
        resultado = dicc[consulta].upper()
        print(f"Su consulta es: {resultado}")
    except KeyError:
        print("Su consulta no esta en la base de datos")

consultas()