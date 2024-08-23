def get_data():
    with open("./data.txt", "r") as f:
      content = f.read().strip().split("\n\n")
      # data = [content[i].split() for i in range(len(content))]
      data = [content[i].split("\n") for i in range(len(content))]
      siatki = []
      for siat in data:
         siatka = []
         for line in siat:
            line_arr = []
            for i in range(len(line)):
               letter = line[i]
               line_arr.append(letter)
            siatka.append(line_arr)
         siatki.append(siatka)
      return siatki


def print_matrix(matrix):
   for i in range(len(matrix)):
      for j in range(len(matrix[0])):
         print(matrix[i][j],
          end="")
      print()



def count_grass(matrix):
   count_grass = 0
   for i in range(len(matrix)):
      for j in range(len(matrix[0])):
         if(matrix[i][j] == "*"):
            count_grass += 1
   return count_grass

      

arr = [".", ".", ".", ".", ".", ".",".", ".", ".", ".", ".", ".","X", ".", ".", ".", ".", "."],[".", ".", "X", ".", ".", ".",".", ".", ".", ".", ".", ".",".", ".", ".", ".", ".", "."],[".", ".", ".", ".", ".", ".",".", ".", ".", ".", ".", ".",".", ".", ".", ".", ".", "."],[".", ".", ".", ".", ".", ".",".", ".", ".", ".", ".", ".",".", ".", ".", ".", ".", "."],[".", ".", "X", ".", ".", ".",".", ".", ".", ".", ".", ".",".", ".", ".", ".", ".", "."],[".", ".", "X", ".", ".", ".",".", ".", ".", ".", ".", ".",".", ".", ".", ".", ".", "."],[".", ".", ".", ".", ".", ".",".", ".", "X", ".", ".", ".",".", ".", ".", ".", ".", "."],[".", ".", ".", ".", ".", ".",".", ".", ".", ".", ".", ".",".", ".", ".", ".", ".", "."]

def max_square_strona_count(matrix):
   strona = 1
   isPossibleToPlaceSquare = True
   i = 0
   while strona < 10000:

      if(strona == len(matrix) + 1 or strona == len(matrix[0]) + 1):
         # print("index bound of array")
         break
      for i in range(0, strona):
         for j in range(0, strona):
            current_title = matrix[i][j]

            # print(i, j)
            if(current_title== "X" or current_title== "x"):
               isPossibleToPlaceSquare = False
               break

            matrix[i][j] = "-"
                      
               
      if(isPossibleToPlaceSquare is True):
         strona += 1
      else:
         # print("max strona: ", strona)
         break
   # print_matrix(matrix)
   return strona - 1

# print(max_square_strona_count(arr))

def main():
   matrixes = get_data()
   max_square = 0
   odp_indexes = []
   i = 1
   for matrix in matrixes:
      square = max_square_strona_count(matrix)
      if(square > max_square):
         max_square = square
         odp_indexes = [i]
      elif(square == max_square):
         odp_indexes.append(i)
      
      i+=1
   print(max_square)
   print(odp_indexes)
      

main()