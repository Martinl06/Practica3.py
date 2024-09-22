def suma():
    try:
        num1 = float(input("Ingresa un numero: "))
        num2 = float(input("Ingresa un segundo numero: "))
        resultado = num1 + num2
        print(f"La suma de {num1} y {num2} es: {resultado}")
    except Exception as e:
        print(f"Ocurrio un error al querer sumar un numero con una cadena de texto {e}")

suma()        
