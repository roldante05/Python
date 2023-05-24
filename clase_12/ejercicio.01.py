import array as arr

num = arr.array('i', range(15, 40, 1))

print(num)

for i in range(len(num)):
    
    if(num[i] % 2 == 0):
        num[i] = 0
        
print(num)