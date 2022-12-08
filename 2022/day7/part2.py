import os 

dir_path = os.path.dirname(os.path.realpath(__file__))
in_file = dir_path + "/input.txt"

class FileStruct:
    def __init__(self, size, name):
        self.name = name
        self.size = size

dir_stack = []

def get_input(file_name):
    f = open(file_name, "r")
    input = str(f.read()).strip()
    f.close()
    return input

def process_input(input):
    input = input.split("\n")
    input.pop(0)
    return input

def take_command(directory_tree, command):
    directory = directory_tree[-1]

    if command == '$ ls':
        return False
    
    command = command.replace('$ cd', '$-cd').split(' ')
    
    if command[0] == 'dir':
        size_file = FileStruct(0, command[1])

        directory.append([size_file])
        dir_stack.append(size_file)

        return False
    if command[0] == '$-cd':
        return command[1]
    
    try:
        file_size = int(command[0])
        directory.append(FileStruct(file_size, command[1]))
        for i in directory_tree:
            i[0].size += file_size
        return False
    except:
        print("Encountered A Non-File Command: " + command[0] + " " + command[1])

def find_directory(dir, name):
    for i in range(1, len(dir)):
        try:
            if dir[i][0].name == name:
                return i
        except:
            pass

def nagivate_system(file_system, data):

    directory_tree = [file_system]

    returned = False
    for i in data:
        returned = take_command(directory_tree,i)
        if returned != False:
            if returned == '..':
                directory_tree.pop(-1)
            else:
                curr_dir = directory_tree[-1]
                directory_tree.append(curr_dir[find_directory(curr_dir,returned)])



def main():

    root_size_file = FileStruct(0, '/')
    file_system = [root_size_file]
    dir_stack.append(root_size_file)

    data = process_input(get_input(in_file))
    nagivate_system(file_system, data)



    total_available_space = 70000000
    required_space = 30000000
    total_used =  root_size_file.size
    remaining_space = total_available_space - total_used
    needed_space = required_space - remaining_space

    min_size = total_used
    
    for i in dir_stack:
        if i.size < min_size and i.size > needed_space:
            min_size = i.size
    
    print(f"The size of the smallest directory needed is {min_size}.")
    
if __name__ == "__main__":
    main()