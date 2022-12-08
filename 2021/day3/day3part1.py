from sys import argv
script, inputfile = argv

def get_input():
     with open(inputfile, 'r') as file:
         return file.readlines()

def to_int(list):
    int_list = []
    for i in list:
        int_list.append(int(i))
    return int_list

data = get_input()
zero = 0
one = 0



for j, k in enumerate(data[0].strip()):

    for i in data:
         if i[j] == '0':
             zero += 1
         if i[j] == '1':
             one += 1

    inc = 0
    for index2, content2 in enumerate(data):
        if content2[-1] == '\n':
            inc += 1

    if inc == 1:
        for aoe in data:
            if "                     " not in aoe:
                print(aoe)
    
    for index, content in enumerate(data):
        if zero < one:
            if content[j] == '1':
                data[index] = "                     "
        elif one < zero:
            if content[j] == '0':
                data[index] = "                     "
        else:
            if content[j] == '1':
                data[index] = "                     "
                        
   # print(data,"\n\n")
    zero = 0
    one = 0

for aoe in data:
    if "                     " not in aoe:
        print(aoe)
#22

