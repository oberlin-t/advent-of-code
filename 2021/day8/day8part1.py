from sys import argv
script, inputfile = argv

def get_input():
    with open(inputfile, 'r') as file:
        return [i.strip().split('|') for i in file.readlines()]

def get1_7_4(data):
    for i in data:
        for j in i.split():
            if len(j) == num_of_segs:
                total += 1
    return total


tot = 0
input = get_input()
tot += count_numof(input, 2)
tot += count_numof(input, 4)
tot += count_numof(input, 3)
tot += count_numof(input, 7)
print(tot)
