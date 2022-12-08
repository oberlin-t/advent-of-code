from sys import argv
import statistics
import math

script, inputfile = argv

def get_input():
    with open(inputfile, 'r') as file:
        return [int(i) for i in file.read().strip().split(',')]

def count_fuel(data,target):
    total = 0
    for i in data:
        total += from_num_to_zero(abs(i - target))
    return total

def from_num_to_zero(a):
    total = 0
    for i in range(a):
        total += a - i
    return total

def find_range(data):
    smallest, biggest = data[0], data[0]
    for i in data:
        if i < smallest:
            smallest = i
        if i > biggest:
            biggest = i
    return range(smallest, biggest + 1)
        

def find_lowest(data,distance):
    lowest = count_fuel(data,data[0])
    for i in distance:
        if count_fuel(data,i) < lowest:
            lowest = count_fuel(data,i)
    return lowest

data = get_input()
mean = statistics.mean(data)

closest = data[0]
smol = abs(data[0] - mean)
for i in data:
    if abs(i - mean) < smol:
        smol = abs(i - mean)
        closest = i

    
print(count_fuel(data, int(mean)))

#print(find_lowest(data,find_range(data)))

