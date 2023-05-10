''' : Escriba un programa que contenga una función con 2 parámetros, llamada multiplicación , la función deberá
poder recibir dos números enteros (int), y luego debe realizar la multiplicación y retornar el valor, luego debe mostrarla'''



def multiplicacion(a1, b1):
   
    resultado = a1 * b1
       
    return resultado


a = int(input('Ingrese un  numero '))
b = int(input('Ingrese un 2do numero '))

print(multiplicacion(a,b))
