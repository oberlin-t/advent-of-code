in_file = "input.txt"

def get_input(file_name):
    f = open(file_name, "r")
    input = str(f.read()).strip()
    f.close()
    return input

def process_input(input):
    input = get_input(in_file).split("\n")

    return input

def get_char(data):
    for i in data[0]:
        for j in data[1]:
            if j == i:
                for k in data[2]:
                    if k == j:
                        return k
        

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

for i in range(0,len(data),3):
    total += points_from(get_char(data[i:i+3]))
    #if points_from(get_char(data[i-3:i])) == None:
     #   print(i)

print(total)