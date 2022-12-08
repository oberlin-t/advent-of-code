from sys import argv
script, inputfile = argv

def get_input():
    with open(inputfile, 'r') as file:
        return [i.strip().split('-') for i in file.readlines()]

def get_other(li, first):
    li.remove(first)
    return li[0]
    
def find_starts(data):
    starts = []
    for i in data:
        if 'start' in i:
            copy_of_i = list([list(j) for j in i])
            copy_of_i.remove(list('start'))
            starts.append(copy_of_i[0])
    return starts

def num_paths(data, start):
    path = [start]
    while True:
        for i in data:
            if path[-1] in i:
                path.append(get_other(i,path[-1]))
        if 'end' in path:
            print(path)

def main():
    data = get_input()
    starts = find_starts(data)
    for i in starts:
        print(data)
        num_paths(data, i)

    
    # for i in range(len(data)):
    #     if 'start' in data[i][0]:
    #         path[0] = data[i][0]
    #         path.append(data[i][1])
            
    #         while 'end' not in path:
    #             last = path[-1]
    #             for j in data:
    #                 if j[0] in last:
    #                     path.append(j[1])
    #             if last in path[-1]:
    #                 break

    print(path)
if __name__ == "__main__":
    main()
    


