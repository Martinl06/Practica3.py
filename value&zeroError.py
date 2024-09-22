def num1():
    return float(input("Ingrese un numero: "))
def num2():
    return float(input("Ingrese un segundo numero: "))

def dividir(a, b):
    if b == 0:
        raise Exception ("No se puede dividir por Cero")
    return a / b

while True:
    try:
        resultado = dividir(num1(), num2())
    except ZeroDivisionError:
        print("No se puede dividir los numeros")
    except ValueError:
        print("Ingrese un numero valido")
    else:
        print(resultado)
        break



