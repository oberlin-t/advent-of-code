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

def check_right(matrix,y,x):
    if matrix[y,x] < matrix[y,x+1]:
        return True

def check_left(matrix,y,x):
    if matrix[y,x] < matrix[y,x-1]:
        return True

def check_up(matrix,y,x):
    if matrix[y,x] < matrix[y-1,x]:
        return True

def check_down(matrix,y,x):
    if matrix[y,x] < matrix[y+1,x]:
        return True

def check_corners(matrix):
    total = 0
    x = len(matrix[0]) - 1 

    if check_right(matrix,0,0) and check_down(matrix,0,0):
        total += matrix[0,0] + 1
    if check_left(matrix,0,x) and check_down(matrix,0,x):
        total += matrix[0, x] + 1

    y = len(matrix) - 1
    x = len(matrix[y]) - 1 

    if check_right(matrix,y,0) and check_up(matrix,y,0):
        total += matrix[last_y, 0] + 1
    if check_left(matrix,y, x) and check_up(matrix,y,x):
        total += matrix[y, x] + 1

    return total

def check_middle(matrix):
    total = 0
    for i in range(1, len(matrix) - 1):
        x = len(matrix[i]) - 1
        if check_up(matrix,i,0) and check_down(matrix,i,0) and check_right(matrix,i,0):
            total += matrix[i,0] + 1
        if check_up(matrix,i,x) and check_down(matrix,i,x) and check_left(matrix,i,x):
            total += matrix[i,x] + 1

        for j in range(1, len(matrix[i]) - 1):
            if check_up(matrix, i, j) and check_down(matrix, i, j) and check_left(matrix, i, j) and check_right(matrix, i, j):
                total += 1 + matrix[i,j]

    return total
        
def check_matrix(matrix):
    total = check_corners(matrix)
    total += check_middle(matrix)

    y = len(matrix) - 1

    #check bottom and top between corners
    for i in range(1, len(matrix[0]) - 1):
        if check_left(matrix,0,i) and check_right(matrix,0,i) and check_down(matrix,0,i):
            total += matrix[0,i] + 1
    for j in range(1, len(matrix[y]) - 1):
        if check_left(matrix,y,j) and check_right(matrix,y,j) and check_up(matrix,y,j):
            #print(matrix[len(matrix) - 1,i])
            total += matrix[len(matrix) - 1,j] + 1 
            
    return total
    
data = parse_input(get_input())
matrix = np.array(data)

print(check_matrix(matrix))


