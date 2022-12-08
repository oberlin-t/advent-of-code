from sys import argv
script, inputfile = argv

def get_input():
     with aopen(inputfile, 'r') as file:
         return file.readlines()

 out = get_input()
 total = 0
prev = out[0]

for i,j in enumerate(out):
     prev = int(out[i])
     nxt = int(out[i+3])
     
     if prev < nxt:
          total += 1

print(total)
     
