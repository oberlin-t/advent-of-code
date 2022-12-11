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
        if len(input[n]) > 1:
            input[n][1] = int(input[n][1])
    
    return input


def draw_pixel(x, cycle_num, screen):

    cycle_num -= 2

    total_pixels = screen.shape[0] * screen.shape[1]
    current_x = cycle_num % screen.shape[1]
    current_y = int((cycle_num - current_x) / screen.shape[1])

    if abs(current_x - x) < 2:
        screen[current_y, current_x] += 1

    print(f"Current X: {current_x} Current Y: {current_y}")

    return screen


def simulate_cpu(instructions):
    x = 1
    cycle_num = 1

    width, height = 40, 6

    screen = np.zeros((height, width), dtype=int)


    for i in range(len(instructions)):

        if len(instructions) > 0:
            instruction = instructions.pop(0)
        
        if 'noop' in instruction:
            cycle_num += 1
            draw_pixel(x, cycle_num, screen)

        elif 'addx' in instruction:
            cycle_num += 1
            draw_pixel(x, cycle_num, screen)
            
            cycle_num += 1
            
            draw_pixel(x, cycle_num, screen)
            x += instruction[1]
            
        #else:
        #    cycle_num += 1
        #    draw_pixel(x, cycle_num, screen)

    return screen
        

def main():
    data = process_input(get_input(in_file))

    screen = simulate_cpu(data)
    
    horizontal_strip = ""

    for i in screen:
        for j in i:
            if j == 0:
                horizontal_strip += ' '
            if j == 1:
                horizontal_strip += '■'
        print(horizontal_strip)
        horizontal_strip = ""

if __name__ == "__main__":
    main()