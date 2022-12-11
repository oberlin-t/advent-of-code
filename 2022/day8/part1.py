import os 
import numpy as np

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
    total = 0

    
    for i, tree in np.ndenumerate(trees):
        counter = 0
        
        for j in range(4):
    
            y = i[1]
            for x in range(i[0]):
                comparison = trees[x,y]
                if comparison >= tree:
                    counter += 1
                    break

            size = trees.shape
            i = rot_coords(i, size)
            trees = np.rot90(trees)

        if counter < 4:
            
            total += 1

    return total
        
def main():
    data = get_input(in_file)
    print(f"The amount of trees visable is {check_visibility(data)}.")
    


if __name__ == "__main__":
    main()