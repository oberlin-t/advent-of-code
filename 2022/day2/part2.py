in_file = "input.txt"

def get_input(file_name):
    f = open(file_name, "r")
    input = str(f.read()).strip()
    f.close()
    return input

def process_input(input):
    input = get_input(in_file).split("\n")

    for i in range(len(input)):
        input[i] = input[i].split(" ")

    return input

def is_a(response): #they played rock
    points = 0

    match response:
        case "X":
            points += 3

        case "Y":
            points += 3
            points += 1
        case "Z":
            points += 6
            points += 2
    return points

def is_b(response): #they played paper
    points = 0

    match response:
        case "X":
            points += 1
        case "Y":
            points += 3
            points += 2
        case "Z":
            points += 6
            points += 3
    return points

def is_c(response): #they played sccisors
    points = 0

    match response:
        case "X":
            points += 2
        case "Y":
            points += 3
            points += 3
        case "Z":
            points += 6
            points += 1
    return points



    
def points_from_round(round_data):

    match round_data[0]:
        case "A":
            return is_a(round_data[1])
        case "B":
            return is_b(round_data[1])
        case "C":
            return is_c(round_data[1])


data = process_input(get_input(in_file))
total = 0
for i in data:
    total += points_from_round(i)

print(total)










