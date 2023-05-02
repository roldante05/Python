import array as arr
import random

val_ini = 0
val_fin = 1000

vector = arr.array('i', range(val_ini, val_fin + 1, 1))

num_eli = int(input(f'ingrese el numero entre {val_ini} y {val_fin} '))

if num_eli in vector:
    
    for pos, elemento in enumerate(vector):
        if num_eli == elemento:
            pos_num_eli = pos
    print(f"Eliminando el elemento con el numero {num_eli} del vector")
    vector.remove(num_eli)
    print("Los elementos anteriores y posteriores son: ", end = ' ')
    if pos_num_eli >= 2:
        print(*vector[pos_num_eli -2 : pos_num_eli + 2])
    else:
        print(*vector[pos_num_eli: pos_num_eli + 2])
else:
    print("El numero ingresado no existe en el vectir")
    
print(f'''El elemento ocupaba la posisicion {pos_num_eli} del vector
El elemento que ocupa esa posicion ahora es el numero: {vector[pos_num_eli]}
''')
    