from sys import argv
script, inputfile = argv

def get_input():
    with open(inputfile, 'r') as file:
        return [int(i) for i in file.read().strip().split(',')]

def fish_days(data):
    for i in range(256):
        print(i)
        data = apply_itteration(data)
    return data
        
def apply_itteration(data):
    for i in range(len(data)):
        data[i] -= 1
        if data[i] < 0:
            data[i] = 6
            data.append(8)
    return data

fish_on_8 = 0
fish_on_7 = 0
fish_on_6 = 0
fish_on_5 = 0
fish_on_4 = 0
fish_on_3 = 0
fish_on_2 = 0
fish_on_1 = 0
fish_on_0 = 0

for i in get_input():
    if i == 6:
        fish_on_6 += 1
    if i == 5:
        fish_on_5 += 1
    if i == 4:
        fish_on_4 += 1
    if i == 3:
        fish_on_3 += 1
    if i == 2:
        fish_on_2 += 1
    if i == 1:
        fish_on_1 += 1
    if i == 0:
        fish_on_0 += 1

for i in range(256):
    buff = fish_on_0
    fish_on_0 = fish_on_1
    fish_on_1 = fish_on_2
    fish_on_2 = fish_on_3
    fish_on_3 = fish_on_4
    fish_on_4 = fish_on_5
    fish_on_5 = fish_on_6
    fish_on_6 = fish_on_7 + buff
    fish_on_7 = fish_on_8
    fish_on_8 = buff

print(fish_on_0+fish_on_1+fish_on_2+fish_on_3+fish_on_4+fish_on_5+fish_on_6+fish_on_7+fish_on_8)
    
