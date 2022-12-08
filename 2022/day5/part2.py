import os 

dir_path = os.path.dirname(os.path.realpath(__file__))
in_file = dir_path + "/input.txt"

def get_input(file_name):
    f = open(file_name, "r")
    input = str(f.read()).strip()
    f.close()
    return input

def process_input(input):
    input = input.split("\n\n")
    input[1] = input[1].split("\n")
    for n, i in enumerate(input[1]):
        input[1][n] = i.replace("move ", '').replace(" from", "-").replace(" to ", "-").split("-")
    return input


def crates_to_stacks(input):
    crates = [[],[],[],[],[],[],[],[],[]]

    input = input.split("\n")
    for i in input:
        for n, j in enumerate(i):
            if j.isalpha():
                v = int((n - 1) / 4)
                a = crates[0]
                crates[v].insert(0, j)

    return crates
    
def move_box(moves, data):
    for i in moves:
        for j in range(int(i[0])):
            data[int(i[2])-1].append(data[int(i[1])-1].pop(   -1 * ((int(i[0]) - j)   )))
    return data

def main():

    

    data = process_input(get_input(in_file))


    crates = crates_to_stacks(data[0])
    crates = move_box(data[1], crates)

    a = ''
    for i in crates:
         a += i[-1]
        
    print(a)

if __name__ == "__main__":
    main()



