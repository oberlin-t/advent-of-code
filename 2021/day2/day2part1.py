from sys import argv
script, inputfile = argv

def get_input():
     with open(inputfile, 'r') as file:
         return file.readlines()


def get_amount_direction(input):
    if input[0] == 'f' :
        return 1, int(input[8])
    if input[0] == 'd':
        return 0, int(input[5])
    if input[0] == 'u':
        return 0, -int(input[3])

depth = 0
horizont = 0
aim = 0

for i in get_input():
    act, much = get_amount_direction(i)
    if act == 0:
        aim += much
    if act == 1:
        horizont += much
        depth += aim * much

        
print(depth * horizont)
        
