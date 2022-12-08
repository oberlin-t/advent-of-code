from sys import argv
import numpy as np
script, inputfile = argv

def get_input():
    with open(inputfile, 'r') as file:
        return [i.strip() for i in file.readlines()]


def parse_input(data):
    new_li = []
    for i in data:
        new_li.append([int(j) for j in i])
    return new_li

    
data = parse_input(get_input())
matrix =  np.array(data)

total = 0

#deal with top line
if matrix[0,0] < matrix[0,1] and matrix[0,0] < matrix[1,0]:
    total += 1 + matrix[0,0]

if matrix[0,len(matrix[0])-1] < matrix[0,len(matrix[0])-2] and matrix[1,len(matrix[0])-1]:
    total += 1 + matrix[0,len(matrix[0])-1]

for i in range(1,len(matrix)-1):
    #side pannels
    if matrix[i,0] < matrix[i-1,0] and matrix[i,0] < matrix[i+1,0] and matrix[i,0] < matrix[i,1]:
        total += 1 + matrix[i,0]
    if matrix[i,len(matrix[i])-1] < matrix[i-1,len(matrix[i])-1] and matrix[i,len(matrix[i])-1] < matrix[i+1,len(matrix[i])-1] and matrix[i,len(matrix[i])-1] < matrix[i,len(matrix[i])-2]:
        total += 1 + matrix[i,len(matrix[i])-1]
    
    for j in range(1,len(matrix[i]) - 1):
        break


#deal with bottom line

if matrix[len(matrix) - 1,0] < matrix[len(matrix) - 2,0] and matrix[len(matrix) - 1,0] < matrix[len(matrix) - 1,1]:
    total += 1 + matrix[len(matrix) - 1,0]
if matrix[len(matrix) - 1,len(matrix[0])-1] < matrix[len(matrix) - 2,len(matrix[0])-1] and matrix[len(matrix) - 1,len(matrix[0])-1] < matrix[len(matrix) - 1,len(matrix[0])-2]:
    total += 1 + matrix[len(matrix) - 1,len(matrix[0])-1]

print(total)






