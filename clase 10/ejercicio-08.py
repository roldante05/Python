'''
Escriba una función para cargar un vector de n cantidad de elementos con valor 0 cero , debe retornar el vector.

'''

def vector(n):
    
   import array as arr
   num = arr.array('i',[])
   
   for i in range(n):
       num.append(0)
       
   return num

print(*vector(5))
    
    
    
    
    
    
    
