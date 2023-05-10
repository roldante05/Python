def saludo_optimista():
    '''Función para mandar un saludo optimista al usuario '''
    import random    
    nom = input('Ingrese su nombre ').capitalize()
    
    s_amables = ["hoy es tu dia de suerte","tu puedes..." , "que tengas una excelente jornada"]
    
    saludos = random.choice(s_amables)
    
    print(f"Hola {nom} {saludos}")

help(len)
