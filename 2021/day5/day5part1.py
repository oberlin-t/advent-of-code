from sys import argv
script, inputfile = argv

def get_input():
    with open(inputfile, 'r') as file:
        return file.readlines()

def parse_to_int(data):
    init_split, convert_to_int = [], []

    for i in data:
        init_split = i.replace(' -> ',',').split(',')
        for j in init_split:
            convert_to_int.append(int(j))
    return convert_to_int


def build_line(data,x1,y1,x2,y2):
    if x1 == x2: #vertical line
        if y1 > y2:
            buffer = y2
            y2 = y1
            y1 = buffer

        for i in range(y1,y2+1):
            data[x1][i] += 1
    elif y1 == y2: #horizontal line
        if x1 > x2:
            buffer = x2
            x2 = x1
            x1 = buffer
            
        for i in range(x1,x2+1):
            data[i][y1] += 1
    else:
         if x1 > x2:
             buffer = x2
             x2 = x1
             x1 = buffer
             buffer = y2
             y2 = y1
             y1 = buffer
             print(x1,y1,x2,y2)
    
         for i in range(x1,x2+1):
             if y1 > y2:
                 data[i][y1 - (1 * (i-x1))] += 1
             if y2 > y1:
                 data[i][y1 + (1 * (i-x1))] += 1
            
    return data
    
data = parse_to_int(get_input())
arraymax = 0

for i in data:
    if int(i) > arraymax:
        arraymax = int(i) + 1

sub_matrix = []
matrix = []
for j in range(arraymax):
    sub_matrix.append(0)
for k in range(arraymax):
    matrix.append(sub_matrix.copy())


for i in range(int(len(data)/4)):
    x1,y1,x2,y2 = data[4*i],data[(4*i)+1],data[(4*i)+2],data[(4*i)+3]
    matrix = build_line(matrix,x1,y1,x2,y2)

total = 0
    
for i, iv in enumerate(matrix):
    for j in matrix[i]:
        if j > 1:
            total += 1

print("Total:",total,'\n')

def print_pretty(data):
    for i, iv in enumerate(data):
        for j, jv in enumerate(data[i]):
            if data[j][i] == 0:
                print('.', end = '')
            else:
                print(data[j][i], end = '')
        print()

#print_pretty(matrix)
