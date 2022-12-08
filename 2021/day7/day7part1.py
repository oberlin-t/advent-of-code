from sys import argv
import statistics

script, inputfile = argv

def get_input():
    with open(inputfile, 'r') as file:
        return [int(i) for i in file.read().strip().split(',')]

def count_fuel(data,target):
    total = 0
    for i in data:
        total += abs(i - target)
    return total

data = get_input()

print(count_fuel(data,int(statistics.median(data))))

