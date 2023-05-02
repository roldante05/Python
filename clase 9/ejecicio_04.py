import random

while True:
    jugar = input('''

\nQuieniela de la suerte\n\n Presione enter para conocer el numero de la suerte
''')
    
    print(f'''
\n Su numero de la suerte es {random.randint(1,99)}
''')
    
    if(jugar == 'apagar'):
        break
    