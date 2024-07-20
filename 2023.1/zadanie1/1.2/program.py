def get_boards():
   with open("./../../data/szachy.txt", "r") as f:
      content = f.read().strip()
      boards = content.split("\n\n")
      finalBoards = []
      for board in boards:
         finalBoards.append(board.split("\n"))
      # print(finalBoards)
      f.close()
      return finalBoards



def isequals(list1, list2):
    list1.sort()
    list2.sort()
    if(len(list1) != len(list2)):
        return False
    for i in range(len(list1)):
        if(list1[i] != list2[i]):
            return False
            break
    return True
    

def get_board_info(board, num):
   count_upper_figures = 0 #white
   count_lower_figures = 0 #black

   upper_list = [] #white
   lower_list = [] #black

   data = []

   for col in range(8):
      for row in range(8):
         if(board[col][row] != "." and board[col][row].isupper()):
            upper_list.append(board[col][row])
            count_upper_figures += 1
         elif(board[col][row] != "." and board[col][row].islower()):
            lower_list.append(board[col][row])
            count_lower_figures += 1

   lower_list = [item.lower() for item in lower_list]
   upper_list = [item.lower() for item in upper_list]
   

   if(isequals(lower_list, upper_list)):
      data.append(count_lower_figures + count_upper_figures)
      
   return data

min_figures = 9999;
right_boards = 0;
boards = get_boards();
for i, board in enumerate(boards):
   data = get_board_info(board, i)
   if(len(data) == 0):
      continue
   
   right_boards += 1
   if(min_figures > data[0]):
      min_figures = data[0]

print(f"right_boards {right_boards} ")
print(f"min_figures {min_figures} ")


with open("./../results/zadanie1_2.txt", "w") as f:
   f.write(f"{right_boards} {min_figures}")
   f.close();
