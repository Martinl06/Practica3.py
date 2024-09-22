def result():
    try:
        numero1 = float(input("Escribe un numero: "))
        numero2 = float(input("Escribe el segundo numero: "))
        resultado = numero1/numero2
        print(f"el resultado de {numero1} dividido {numero2} es :{resultado}")
    except ZeroDivisionError:
        print("Ha ocurrido un error al dividir por cero")    

result()
