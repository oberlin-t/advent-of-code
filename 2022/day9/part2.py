import os 
import numpy as np
import copy

dir_path = os.path.dirname(os.path.realpath(__file__))
in_file = dir_path + "/input.txt"

knots = 10

def get_input(file_name):
    f = open(file_name, "r")
    input = str(f.read()).strip()
    f.close()
    return input

def process_input(input):
    input = input.split("\n")
    for n, i in enumerate(input):
        input[n] = i.split(" ")
        input[n][1] = int(input[n][1])
    
    return input

def get_size(input):
    max_x = 0
    min_x = 0
    max_y = 0
    min_y = 0

    x = 0
    y = 0

    for i in input:
        amount = i[1]
        symbol = i[0] 
        if symbol == 'R':
            x += amount
        if symbol == 'L':
            x -= amount
        if symbol == 'U':
            y += amount
        if symbol == 'D':
            y -= amount
        
        if x > max_x:
            max_x = x
        elif x < min_x:
            min_x = x
        if y > max_y:
            max_y = y
        if y < min_y:
            min_y = y

    return(min_x, max_x, min_y, max_y) 

def make_canvas(width, height):
    canvas = list()
    for x in range(width):
        canvas.append([])
        for y in range(height):
            canvas[x].append(['.'])

    return canvas

def dist_greater_than_one(x1,y1,x2,y2):
    x_diff = abs(x2-x1)
    y_diff = abs(y2-y1)

    if x_diff > 1 or y_diff > 1:
        return True

    return False

def apply_dir(direction, index, coords):
        if direction == 'R':
            coords[index][0] += 1
        elif direction == 'L':
            coords[index][0] -= 1
        elif direction == 'U':
            coords[index][1] += 1
        elif direction == 'D':
            coords[index][1] -= 1

def clense_nums(canvas, index1, index2):
    try:
        canvas[index1][index1].pop()
    except:
        pass

def draw(coords, canvas):
    temp = copy.deepcopy(canvas)
    
    for i in range(knots):
        a = temp[coords[i][0]][coords[i][1]] 
        temp[coords[i][0]][coords[i][1]][0] = str(i)
    return temp

    
def hash_mark(coords, canvas):
    if '#' not in canvas[coords[-1][0]][coords[-1][1]]:
        canvas[coords[-1][0]][coords[-1][1]].append('#')

def update_location(command, coords, canvas):
    #head_x = coords[0][0]
    #head_y = coords[0][1]
    #tail_x = coords[-1][0]
    #tail_y = coords[-1][1]

    direction = command[0]

    for step in range( command[1]):

        #clense_nums(canvas, coords[0][0], coords[0][1])
        apply_dir(direction, 0, coords)

        for knot in range(1, knots):
            knot_x, knot_y, prev_x, prev_y = coords[knot][0], coords[knot][1], coords[knot-1][0], coords[knot-1][1]
            if dist_greater_than_one(knot_x, knot_y, prev_x, prev_y):
                """   if knot_x == prev_x or knot_y == prev_y:
                #clense_nums(canvas, coords[knot][0], coords[knot][1])
                    apply_dir(direction, knot, coords)
                else: """

                x_diff = prev_x - knot_x
                y_diff = prev_y - knot_y
                if abs(x_diff) > 1:
                    x_diff /= 2
                if abs(y_diff) > 1:
                    y_diff /= 2
                
                coords[knot][0] += int(x_diff)
                coords[knot][1] += int(y_diff)

                hash_mark(coords, canvas)
                
                    
def print_canvas(canvas):
    for i in canvas:
        print(i)


        


def execute_instruction(canvas, data, starting_point):
    
    
    coords = list()

    for i in range(knots):
        coords.append([starting_point[0], starting_point[1]])
    
    canvas[starting_point[0]][starting_point[1]][0] = 's'
    
    """ head_x = coords[0][0]
    head_y = coords[0][1]
    tail_x = coords[-1][0]
    tail_y = coords[-1][1] """

    for command in data:
        direction = command[0]
        
        update_location(command, coords, canvas)

    
            




def main():
    data = process_input(get_input(in_file))
    max_and_min = get_size(data)

    width = max_and_min[1] - max_and_min[0]
    height = max_and_min[3] - max_and_min[2]

    starting_point = (-max_and_min[0], -max_and_min[2])
    canvas = make_canvas(width + 1, height + 1)

    execute_instruction(canvas, data, starting_point)
    flat = np.asarray(canvas, dtype=object).flatten()
     
    total = 0

    for i in flat:
        if '#' in i or 's' in i:
            total += 1


    print(f"The total number of positions the tail rope visited is {total}.")
    


if __name__ == "__main__":
    main()