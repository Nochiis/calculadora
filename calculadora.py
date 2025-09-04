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



