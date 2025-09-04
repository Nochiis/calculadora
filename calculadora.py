def suma (x, y):
    return x + y

def resta (x, y):
    return x - y

def multiplicación(x, y):
    return x * y

def division(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "No puedes hacer la división por cero"



print("************************************")
print("         MI CALCULADORA             ")
print("************************************")
print("1. SUMA")
print("2. RESTA")
print("3. MULTIPLICACIÓN")
print("4. DIVISION")
print("************************************")



