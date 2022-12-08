from sys import argv
script, inputfile = argv

def get_input():
     with open(inputfile, 'r') as file:
         return file.readlines()

