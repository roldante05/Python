''' Escriba un programa permite ingresar dos números enteros por teclado, luego debe resolver la división de los
dos números por medio de una función, la función deberá corroborar que los números (argumentos) no sean ceros antes de
realizar la división, si los valores son correctos debe retornar el resultado de la división con comas pero si alguno de los
valores es cero deberá retornar un string con la palabra Error. muestre por pantalla el resultado '''


def division(a1, b2):
    if a1 == 0 or b2 == 0:
        return"Error"

    else:
        return a1 / b2

a = int(input('Ingrese un numero '))
b = int(input('Ingrese un 2do numero '))

print(division(a, b))