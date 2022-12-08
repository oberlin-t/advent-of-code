in_file = "input.txt"

def get_input(file_name):
    f = open(file_name, "r")
    input = str(f.read()).strip()
    f.close()
    return input

def process_input(input):
    input = get_input(in_file).split("\n")

    for n, i in enumerate(input):
        input[n] = [ i[0:int(len(i)/2)],i[int(len(i)/2):int(len(i))]]

    return input

def get_char(compartments):
    for i in compartments[0]:
        for j in compartments[1]:
            if i == j:
                return i

def points_from(in_char):
    lower_alphabet = list(enumerate("abcdefghijklmnopqrstuvwxyz", 1))
    upper_alphabet = list(enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 27))
    
    for i in lower_alphabet:
        if i[1] == in_char:
            return i[0]

    for i in upper_alphabet:
        if i[1] == in_char:
            return i[0]


data = process_input(get_input(in_file))    

total = 0

for i in data:
    total += points_from(get_char(i))

print(total)
