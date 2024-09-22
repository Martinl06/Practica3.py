import datetime

def registroErrores(archivo_N):
    try:
        with open(archivo_N, "r") as archivo:
            contenido = archivo.read()    
            print("El contenido es: ")
            print(contenido)
        
    except FileNotFoundError:
        registro = datetime.datetime.now()
        formatoFecha = registro.strftime("%d-%m-%Y_%H-%M-%S")
        nombreArchivo = f"err_{formatoFecha}.txt"

        with open(nombreArchivo, "w") as archivo:
            archivo.write(f"{archivo_N}")
            print(f"El archivo seleccionado no existe, se ha creado el mismo {archivo_N} a la base de datos")

archivo_N = input("Seleccione el archivo: ")
registroErrores(archivo_N)          

        


