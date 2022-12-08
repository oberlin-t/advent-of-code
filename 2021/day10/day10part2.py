from sys import argv
script, inputfile = argv

def get_input():
    with open(inputfile) as file:
        return [i.strip() for i in file.readlines()]

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
                return False
    return queue

def points_from_queue(queue):
    points = 0
    for i in reversed(queue):
        points = points * 5
        if i == '[':
            points += 2
        if i == '(':
            points += 1
        if i == '{':
            points += 3
        if i == '<':
            points += 4
    return points
    
data = get_input()
point_list = []

for i in data:
    line_data = check_line(i)
    if line_data != False:
        point_list.append(points_from_queue(check_line(i)))

point_list.sort()
print(point_list[int(len(point_list)/2)])
