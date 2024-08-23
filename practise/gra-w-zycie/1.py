def get_data():
    with open("./data.txt", "r") as f:
      content = f.read().strip().split("\n")
      # siatka = [content[i].split() for i in range(len(content))] 
      siatka = []
      for line in content:
         arr = []
         for i in range(len(line)):
            arr.append(line[i])
         siatka.append(arr)
         
      return siatka

#print(data[5][9])
# 5 - stroka
# 9 - colonka 

class Coords:
    def __init__(self):
        self.x = None
        self.y = None


def get_neighbors(arr, coords):
   y = coords[0]
   x = coords[1]
   answer_coords = []
   neighbors_vectors = [(1,0), (-1,0), (0,1), (0,-1), (1,1), (-1,1), (1,-1), (-1,-1)]
   for vector in neighbors_vectors:
      new_y = y + vector[1]
      new_x = x + vector[0]

      # print("before", new_y, new_x)

      if(new_y >= len(arr)):
         new_y = 0
      if(new_x >= len(arr[0])):
         new_x = 0

      if(new_y < 0):
         new_y = len(arr) - 1
      if(new_y < 0):
         new_y = len(arr[0]) - 1

      # print("after", new_y, new_x, arr[new_y][new_x])
      
      answer_coords.append(arr[new_y][new_x])
   return answer_coords

def print_matrix(matrix):
    for row in matrix:
        for element in row:
            print(element, end=' ')
        print()

def count_neighbors(arr):
   counter = 0

   for item in arr:
      if(item == "X"):counter += 1

   return counter 

def one_generation(data):
   cols = len(data)
   rows = len(data[0])
   alive_coords = []
   dead_coords = []
   # i == y
   # j == x
   for i in range(cols):
      for j in range(rows):
         item = data[i][j]
         # if(item == "X"):print("X", i,j)
         neighbors_arr = get_neighbors(data, (i,j))
         neighbors_count = count_neighbors(neighbors_arr)

         if(item == "." and neighbors_count == 0):
            continue
         if(item == "X" and neighbors_count in [2,3]):
            continue

         if(item == "." and neighbors_count == 3):
            alive_coords.append((i,j))
            continue

         if(item == "X" and neighbors_count > 3 or neighbors_count < 2 ):
            dead_coords.append((i,j))
            continue

   # print("dead: ",dead_coords)
   # print("alive: ", alive_coords)
   for cords in alive_coords:
      data[cords[0]][cords[1]] = "X" 
   for cords in dead_coords:
      data[cords[0]][cords[1]] = "." 
   # print_matrix(data)
   return data
   

def main():
   data = get_data()
   
   i = 0
   while i != 37:
      one_generation(data)
      i+= 1
   print_matrix(data)
   print(get_neighbors(data,(19,2)))
   

   # print(get_neighbors(data, (0, 9)))
   # print(data[11][19])

main()