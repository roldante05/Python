cont = 0
while True:
    num = int(input('Ingrese un numero '))
    if(num == 0):
        print('programa terminado')
        break
    cont += 1
    print(f"{cont} - numero: {num}")