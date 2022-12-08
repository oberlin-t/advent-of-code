import numpy as np
from sys import argv
script, input_file = argv

def clean_negatives(data):
    for k in range(len(data)):
        for l in range(len(data[k])):
            if data[k,l] < 0:
                data[k,l] = 0
    return data

def step(data, total):
    for i in range(len(data)):
        for j in range(len(data[i])):
            data, total = flash(data, total, i, j)
            
    return data, total

def flash(data, total, i, j):
    if data[i,j] > 9 and data[i,j] < 5000:
        total += 1
        data[i,j] = -5000
        data, total = check_around(data, total, i, j)

    return data, total

def check_around(data, total, i, j):
    k, l = i, j
    
    k += 1
    data[k,l] += 1
    data, total = flash(data, total, i, j)
    l += 1
    data[k,l] += 1
    data, total = flash(data, total, i, j)
    l -= 2
    data[k,l] += 1
    data, total = flash(data, total, i, j)

    k, l = i, j
    l += 1
    data[k,l] += 1
    data, total = flash(data, total, i, j)
    l -= 2
    data[k,l] += 1
    data, total = flash(data, total, i, j)

    k, l = i, j
    k -= 1
    data[k,l] += 1    
    data, total = flash(data, total, i, j)
    l += 1
    data[k,l] += 1
    data, total = flash(data, total, i, j)
    l -= 2
    data[k,l] += 1
    data, total = flash(data, total, i, j)

    return data, total
    
def main():
    initial_input = np.genfromtxt(input_file, dtype = int, delimiter = 1)
    data = np.pad(initial_input, 1, constant_values = 5000)

    iterations = 100
    total = 0
    

    for i in range(iterations):
        data = data.__add__(1)
        for times in range(100):
            data, total = step(data, total)
        data = clean_negatives(data)
        
    print(total)
    #print(data)
        
if __name__=="__main__":
    main()

