import copy

def find_starts(data):
    starts = []
    for i in data:
        if 'start' in i:
            i.remove('start')
            starts.append(i[0])
    return starts

def main():
    dat = [['start', 'A'], ['start', 'B'], ['a', 'b']]
    new_dat = copy.deepcopy(dat)
    find_starts(new_dat)
    print(dat)
    
if __name__ == "__main__":
    main()
    


