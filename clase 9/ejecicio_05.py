import random

abc = list('abcdefghijklmnñopqsrtuwxyz')

while True:
    if len(abc) == 0:
        print('El juego ha terminado')
        break
    else:
        jugar=input('\n TUTI FRUTI\n\n Presione enter para ver la letra ')
        letelegida= random.choice(abc)
        print(f"\n La letra es {letelegida.upper()}")
        abc.remove(letelegida)
        print("\n",*abc, "\n\n", len(abc))
