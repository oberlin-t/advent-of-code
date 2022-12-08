f = open("input.txt", "r")
input = str(f.read())
f.close()


input = input.split("\n\n")

for n, i in enumerate(input):
    input[n] = i.strip().split("\n")

one_max = 0
two_max = 0
three_max = 0
temp = 0
print(input)
for elf in input:
    for food in elf:
        temp += int(food)
    if temp > one_max:
        three_max = two_max
        two_max = one_max
        one_max = temp
        
    elif temp > two_max:
        three_max = two_max
        two_max = temp
    elif temp > three_max:
        three_max = temp
    temp = 0

print(
"""
Most Calories on Elf = {}
Second Most Calories on Elf = {}
Third Most Calories on elf = {}
Total = {}       
""".format(one_max, two_max, three_max, one_max+two_max+three_max))
