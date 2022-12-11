import os 


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

def update_signal(signal_strength, total, cycle_num, x):
    if (cycle_num - 20) % 40 == 0:
        
        
        signal_strength = x * cycle_num
        total += signal_strength
        print(f"Cycle Number: {cycle_num} X: {x} Signal Strength: {signal_strength}")

    return signal_strength, total


def simulate_cpu(instructions):
    signal_strength = 0
    x = 1
    cycle_num = 1
    total = 0


    for i in range(len(instructions) + 2):

        if len(instructions) > 0:
            instruction = instructions.pop(0)
        
        if 'noop' in instruction:
            cycle_num += 1
            signal_strength, total = update_signal(signal_strength, total, cycle_num, x)

        elif 'addx' in instruction:
            cycle_num += 1
            signal_strength, total = update_signal(signal_strength, total, cycle_num, x)
            
            cycle_num += 1
            x += instruction[1]
            signal_strength, total = update_signal(signal_strength, total, cycle_num, x)
            
        else:
            cycle_num += 1
            signal_strength, total = update_signal(signal_strength, total, cycle_num)

        
       



    return total


        

def main():
    data = process_input(get_input(in_file))
        
    print(simulate_cpu(data))

if __name__ == "__main__":
    main()