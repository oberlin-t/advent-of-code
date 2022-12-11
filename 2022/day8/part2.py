import os 
import numpy as np
import math

dir_path = os.path.dirname(os.path.realpath(__file__))
in_file = dir_path + "/input.txt"

def get_input(file_name):
    file_data = np.genfromtxt(file_name, dtype=int, delimiter=1)
    return file_data

def rot_coords(coords, size):
    x = size[1] - coords[1] - 1
    y = coords[0]
    return (x,y)

def check_visibility(trees):
    high_score = 0

    
    for i, tree in np.ndenumerate(trees):
        score = 0
        scenic_array = []

        for j in range(4):
            
            scenic_array.append(0)

            y = i[1]
            
            for x in range(i[0] -1,-1, -1):
                comparison = trees[x,y]
                scenic_array[j] += 1
                if comparison >= tree:
                    break


            size = trees.shape
            i = rot_coords(i, size)
            trees = np.rot90(trees)

        score = math.prod(scenic_array)
        if score > high_score:
            high_score = score
            



    return high_score
        
def main():
    data = get_input(in_file)
    print(f"The maximum number of trees visable from any tree is {check_visibility(data)}.")
    


if __name__ == "__main__":
    main()