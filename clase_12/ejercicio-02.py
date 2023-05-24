import array as arr

alumnos=['JUANMARTIN','JUANMANUEL','TIZIANASELENA','TOBIASEZEQUIEL','LAUTARO','THIAGO EZEQUIEL','EZEQUIEL','ALEXLAUTARO','CLAUDIAFIORELLA','TAMARAGISELA','LAURAMAGALI','DANTE ISAAC','LAUTAROEZEQUIEL','JOSEIGNACIO','GUSTAVOJAVIER','GUILLERMOAGUSTIN','ALEX MIGUEL','ERICAGUSTIN','SANTIAGOAGUSTIN','CRISTIANOMAR','LEANDROEMANUEL','ESTEBAN', 'RAMIROGUSTAVO','DAIRAAYLÉN','GONZALODAMIAN','AGUSTINAALEJANDRA','CAMILALUJÁN', 'TOMAS','LAURA','TOBIASCATRIEL','MARCOLEÓN','GABRIEL','TOBIASEZEQUIEL','RITABEATRIZ', 'PATRICIOABRAHAM','ARIELALESSANDRO','GUSTAVOALVARO','AYELÉNALEJANDRA','BRIANTOBIAS']

vec_numeracion = arr.array('i',[0]*len(alumnos))


def cargar(lista):
    for pos in range(len(lista)):
        vec_numeracion[pos] = pos+100
    #print(*vec_numeracion )
    

def mostrar(lista, vec):
    contador=0
    for pos, i in enumerate(lista):  
        print(f"{vec[pos]} | {i}")
    
    


cargar(alumnos)

mostrar(alumnos, vec_numeracion)

