f = open("input.txt", "r")
input = str(f.read()).strip()
f.close()


input = input.split("\n\n")

for n, i in enumerate(input):
    input[n] = i.split("\n")

max = 0
temp = 0
for elf in input:
    for food in elf:
        temp += int(food)
    if temp > max:
        max = temp
    temp = 0

print("Most Calories on Elf = " + str(max))
