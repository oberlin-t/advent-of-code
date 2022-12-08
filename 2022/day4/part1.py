in_file = "input.txt"

def get_input(file_name):
    f = open(file_name, "r")
    input = str(f.read()).strip()
    f.close()
    return input

def process_input(input):
    input = get_input(in_file).replace("-", ",").split("\n")

    for n, i in enumerate(input):
        input[n] = input[n].split(",")
        for j, k in enumerate(input[n]):
            input[n][j] = int(input[n][j])

    return input

def check_line(data):
    n = data[1] - data[0]
    m = data[3] - data[2]
    if n >= m:
        if (data[0] + n) >= data[3] and data[0] <= data[2]:
            return 1
    elif (data[2] + m) >= data[1] and data[2] <= data[0]:
        return 1

    return 0

total = 0

data = process_input(get_input(in_file))
for i in data:
    total += check_line(i)

print(total)