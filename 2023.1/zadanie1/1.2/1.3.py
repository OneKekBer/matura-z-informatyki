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


def handle_board(board):
   for col in range(8):
      for row in range(8):
         if(board[col][row] == "w"):
            print("")      
            

def main ():      
   boards = get_boards()
   for board in boards:
      handle_board(board)
   with open("./../results/zadanie1_3.txt", "w") as f:
      # f.write(f"{right_boards} {min_figures}")
      f.close();


main()

