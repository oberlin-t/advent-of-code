from sys import argv
script, inputfile = argv

def get_input():
    with open(inputfile) as file:
        return [i.strip() for i in file.readlines()]

def points_from_char(c):
    if c == ')':
        return 3
    if c == ']':
        return 57
    if c == '}':
        return 1197
    if c == '>':
        return 25137

def is_open(i):
    if i in ['(','<','[','{']:
        return True
        
def matches(a,b):
    if a == ')' and b == '(':
        return True
    if a == ']' and b == '[':
        return True
    if a == '}' and b == '{':
        return True
    if a == '>' and b == '<':
        return True
    
def check_line(a):
    queue = []
    for i in a:
        if is_open(i):
            queue.append(i)
        else:
            if matches(i,queue[-1]):
                queue.pop(-1)
            else:
                return points_from_char(i)
    return 0
    
data = get_input()
total = 0

for i in data:
    total += check_line(i)
print(total)
