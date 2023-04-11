estado = True
aumenta = ''

while estado:
    rta = input("Seleccione: (A)celarar, (S)alir ").lower()
    if(rta == 'a'):
        aumenta +='n'
        print(f"Aceleran{aumenta}do")
    elif(rta != 's'):
        print("Opcion no valida intente de nuevo")
    else:
        print("Parar")
        estado = False
        