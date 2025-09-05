def suma (x, y):
    return x + y

def resta (x, y):
    return x - y

def multiplicacion(x, y):
    return x * y

def division(x, y):
    try:
        return x / y
    except ZeroDivisionError as e:
        return "NO SE PUEDE DIVIDIR EN ZERO"
    
    
def operacion(o, a, b):
    if o == 1:
        print("LA SUMA ES: ", suma(a, b))
    elif o == 2:
        print("LA RESTA ES: ", resta(a, b))
    elif o == 3:
        print("LA MULTIPLICACION ES: ", multiplicacion(a, b))
    elif o == 4:
        print("LA DIVISION ES: ", division(a, b))    
    elif o == 5:
        print("SALIENDO...")
        return False
    else:
        print("OPCION INVALIDA.")


print("************************************")
print("         MI CALCULADORA             ")
print("************************************")
print("1. SUMA")
print("2. RESTA")
print("3. MULTIPLICACIÓN")
print("4. DIVISION")
print("5. SALIR")
print("************************************")

op = int(input("SELECCIONA UNA OPERACION: "))
a =  int(input("DIGITA EL PRIMER NUMERO: "))
b =  int(input("DIGITA EL SEGUNDO NUMERO: "))

operacion(op, a, b)
 