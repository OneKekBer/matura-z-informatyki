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
         print(matrix[i][j], end="")
      print()


def count_grass(matrix):
   count_grass = 0
   for i in range(len(matrix)):
      for j in range(len(matrix[0])):
         if(matrix[i][j] == "*"):
            count_grass += 1
   return count_grass



def main():
   matrixes = get_data()
   count = 0
   for matrix in matrixes:
      max_length = len(matrix) * len(matrix[0])
      # print(max_length)
      grass_count = count_grass(matrix)

      grass_procent = 70 * max_length // 100
      # print(grass_procent)
      if(grass_count >= grass_procent):
         count += 1
         print_matrix(matrix)
      

   print(count)
main()