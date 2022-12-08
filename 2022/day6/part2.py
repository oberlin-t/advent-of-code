import os 

dir_path = os.path.dirname(os.path.realpath(__file__))
in_file = dir_path + "/input.txt"

def get_input(file_name):
    f = open(file_name, "r")
    input = str(f.read()).strip()
    f.close()
    return input

def is_not_repeating(data):
    total = 0
    for i in data:
        total = 0
        for j in data:
            if i == j:
                total += 1
        if total > 1:
            return False
    return True


def main():
    data = get_input(in_file)

    num_chars = 14

    for i in range(len(data) - num_chars + 1):
        num_range = data[i:i+num_chars]
        if is_not_repeating(num_range):
            print(i + num_chars)
            break
            




if __name__ == "__main__":
    main()