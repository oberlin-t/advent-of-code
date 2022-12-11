import os 
import numpy as np

dir_path = os.path.dirname(os.path.realpath(__file__))
in_file = dir_path + "/input.txt"

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
            canvas[x].append([])

    return canvas

def dist_greater_than_one(x1,y1,x2,y2):
    x_diff = abs(x2-x1)
    y_diff = abs(y2-y1)

    if x_diff > 1 or y_diff > 1:
        return True

    return False

def update_out_of_bounds(canvas, coords, last_coords):
    if dist_greater_than_one(coords[0][0], coords[0][1], coords[1][0], coords[1][1]):
        coords[1][0] = last_coords[0]
        coords[1][1] = last_coords[1]

def execute_instruction(canvas, data, starting_point):

    coords = list()
    coords.append([starting_point[0], starting_point[1]])
    coords.append([starting_point[0], starting_point[1]])

    for command in data:
        direction = command[0]
        for step in range(command[1]):

            if '#' not in canvas[coords[1][0]][coords[1][1]]:  # add markers where its been
                canvas[coords[1][0]][coords[1][1]].append('#')

            if direction == "L":
                last_coords = coords[0].copy()
                coords[0][0] -= 1
                update_out_of_bounds(canvas, coords, last_coords)

            elif direction == "R":
                last_coords = coords[0].copy()
                coords[0][0] += 1
                update_out_of_bounds(canvas, coords, last_coords)

            elif direction == "U":
                last_coords = coords[0].copy()
                coords[0][1] += 1
                update_out_of_bounds(canvas, coords, last_coords)
            elif direction == "D":
                last_coords = coords[0].copy()
                coords[0][1] -= 1
                update_out_of_bounds(canvas, coords, last_coords)




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
        if '#' in i:
            total += 1

    print(f"The total number of positions the tail rope visited is {total}.")



if __name__ == "__main__":
    main()