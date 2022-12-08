from sys import argv
import numpy as np
script, inputfile = argv
matrix = np.pad(np.genfromtxt(inputfile, dtype = int, delimiter = 1), 1,constant_values = 9)

def check_pos(matrix,y,x):
    total = 0
    if matrix[y,x] == 9:
        return 0
    
    target = matrix[y,x]
    above = matrix[y-1,x]
    below = matrix[y+1,x]
    left = matrix[y,x-1]
    right = matrix[y,x+1]

    is_minimum = target <= above and target <= below and target <= left and target <= right 
    if is_minimum:
        total += 1
        matrix[y,x] = 9
        
        total += check_pos(matrix,y+1,x)
        total += check_pos(matrix,y-1,x)
        total += check_pos(matrix,y,x+1)
        total += check_pos(matrix,y,x-1)
    return total

def find_low(matrix):
    first = 0
    second = 0
    third = 0
    for i in range(1, len(matrix) - 1):
        for j in range(1, len(matrix[i]) - 1):
            output = check_pos(matrix,i,j)
            if output > first:
                third = second
                second = first
                first = output
            elif output > second:
                third = second
                second = output
            elif output > third:
                third = output
                
    return first, second, third

big, less, lessest = find_low(matrix)
print(big*less*lessest)

             

