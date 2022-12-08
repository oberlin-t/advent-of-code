from sys import argv
script, inputfile = argv

def get_input():
    with open(inputfile, 'r') as file:
        return [i.strip().split('|') for i in file.readlines()]
    
def get1_4_7_8(data):
    one_str, four_str, sev_str, eight_str = '','','',''
    
    for i in data.split():
        if len(i) == 2:
            one_str = i
        if len(i) == 4:
            four_str = i
        if len(i) == 3:
            sev_str = i
        if len(i) == 7:
            eight_str = i
    return one_str, four_str, sev_str, eight_str

def many_in_common(str1, str2):
    total = 0
    for i in str1:
        if i in str2:
            total += 1
    return total

def get2(data, four_string):
    for i in data.split():
        total = 0
        if len(i) == 5:
            if many_in_common(i, four_string) == 2:
                return i

def get_3_5(data, two_string):
    three_str, five_str = '',''
    for i in data.split():
        if len(i) == 5:
            if many_in_common(i, two_string) == 4:
                three_str = i
            elif many_in_common(i, two_string) == 3:
                five_str = i
    return three_str, five_str

def get_0_6_9(data, four_string, one_string):
    zero_str, six_str, nine_str = '','',''
    for i in data.split():
        if len(i) == 6:
            if many_in_common(i, one_string) == 1:
                six_str = i
            elif many_in_common(i, four_string) == 4:
                nine_str = i
            else:
                zero_str = i
    return zero_str, six_str, nine_str

def equiv_messages(str1, str2):
    if len(str1) == len(str2):
        if many_in_common(str1, str2) == len(str1):
            return True
    return False

input = get_input()

total_total = 0
totaliv = '0'

for i in input:
    totaliv = ''
    key = []
    v1_4_7_8 = get1_4_7_8(i[0])
    v2 = get2(i[0],v1_4_7_8[1])
    v3_5 = get_3_5(i[0], v2)
    v0_6_9 = get_0_6_9(i[0],v1_4_7_8[1],v1_4_7_8[0])
    key.append(v0_6_9[0])
    key.append(v1_4_7_8[0])
    key.append(v2)
    key.append(v3_5[0])
    key.append(v1_4_7_8[1])
    key.append(v3_5[1])
    key.append(v0_6_9[1])
    key.append(v1_4_7_8[2])
    key.append(v1_4_7_8[3])
    key.append(v0_6_9[2])
    
    for j in i[1].split():
        for i, iv in enumerate(key):
            if equiv_messages(j, iv):
                totaliv += str(i)
    total_total += int(totaliv) 
print(total_total)

