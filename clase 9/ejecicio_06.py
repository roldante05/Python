import array as arr

num = arr.array('i', range(50, 71, 1))

for pos, i in  enumerate(num):
    if pos ==  15:        
        print(i)
        