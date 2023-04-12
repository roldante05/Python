pase = True

while pase:
    n1 = int(input('Ingrese un numero '))
    if(n1 == 0):
        print('Programa finalizado')
        pase = False
    elif (n1 > 100):
        print('Invalido intente de nuevo')
        continue
    elif (n1 % 2 == 0):
        print(f'El numero {n1}  es par')
        break
    else:
        print('El numero {n1} es impar')
        break