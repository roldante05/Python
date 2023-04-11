cont = 0
acum = 0
while True:
    num = float(input('Ingrese un numero '))
   
    if(num == 0):
        print('programa terminado')
        break
    acum += num
    cont += 1
    print(f"{cont} - ingreso: {num:.2f} acumulado {acum} ")