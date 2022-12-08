from sys import argv
script, inputfile = argv

def get_input():
     with open(inputfile, 'r') as file:
         data = file.readlines()
         stripped = []
         for i in data:
             stripped.append(i.strip())
         return stripped

def split_list(list,splitter):
     new_list = []
     last_split = 0
     for i,j in enumerate(list):
          if j == splitter:
               new_list.append(list[last_split:i])
               last_split = i + 1
     new_list.append(list[last_split:len(list)])
     return new_list


def str_to_intlist(list):
     for i, j in enumerate(list):
          list[i] = list[i].split()
          for k,kv in enumerate(list[i]):
               list[i][k] = int(kv)
     return list

def add_toggled_proporty(list):
     for i, iv in enumerate(list):
          for j, jv in enumerate(list[i]):
               for k, kv in enumerate(list[i][j]):
                    list[i][j][k] = [kv, False]
     return list

def mark_numbers(list ,input_number):
     for i, iv in enumerate(list):
          for j, jv in enumerate(list[i]):
               for k, kv in enumerate(list[i][j]):
                    if kv[0] == input_number:
                         list[i][j][k][1] = True
     return list

def winning_board(list, i, last_number):
     total = 0
     for j, jv in enumerate(list[i]):
          for k, kv in enumerate(list[i][j]):
               if list[i][j][k][1] == False:
                    total += kv[0]
                    
     print("Winning Score:", total*last_number, "Board Number:", i + 1, "Total:", total, "Last Num:", last_number)   
     

def check_horz(list, last_number):
     global boards
     for i, iv in enumerate(list): # for each board
          for j, jv in enumerate(list[i]): # for each horizontal line in the board
               total = 0
               for k, kv in enumerate(list[i][j]): # for each term in the each line
                    if list[i][j][k][1] == True:
                         total += 1
               if total == 5:
                    winning_board(list,i,last_number)
                    boards[i] = []
                    break
                    
def check_vert(list, last_number):
     global boards
     for i, iv in enumerate(list):
          for k,kv in enumerate(range(5)):
               total = 0
               for j,jv in enumerate(list[i]):
                    if list[i][j][k][1] == True:
                         total += 1
               if total == 5: 
                    winning_board(list, i, last_number)
                    boards[i] = []
                    break
                    
data = get_input()
numbers_as_str = data[0].split(',')
boards = add_toggled_proporty(split_list(str_to_intlist(data[2:]),[]))

for i in numbers_as_str:
     boards = mark_numbers(boards, int(i)) 
     check_horz(boards, int(i))
     check_vert(boards, int(i))
