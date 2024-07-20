textFromFile = ""


def count_columns(board, i):
    empty_columns = 0
    for col in range(8):
        is_empty = True;
        for row in range(8):
            if(board[row][col] != "."):
                is_empty = False
                break;
        if(is_empty):
            empty_columns += 1  
    return empty_columns

def get_board():
    with open("./../data/szachy_przyklad.txt", "r") as f:
        content = f.read().strip()
        boards = content.split("\n\n")
        finalBoards = []
        for board in boards:
            finalBoards.append(board.split("\n"))
        return finalBoards

def main():
    boards = get_board()
    for i, board in enumerate(boards):
        number_of_columns = count_columns(board, i)
        print(number_of_columns)
    
main()