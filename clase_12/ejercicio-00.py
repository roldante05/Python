import array as arr

num = arr.array('i', range(73, 173, 1))

pos1 = 0
pos2 = 0


for pos, i in enumerate(num):
    if i == 90:
        pos1 = pos
    elif i == 106:
        pos2 = pos
        
print(num[pos1:pos2])


