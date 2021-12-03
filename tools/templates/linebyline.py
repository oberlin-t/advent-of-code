from sys import argv
script, inputfile = argv

def getInput():
     with open(inputfile, 'r') as file:
         return file.readlines()

