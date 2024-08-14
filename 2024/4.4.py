def get_data():
   with open("./data/plansza.txt", "r") as f:
      content = f.read().strip().split("\n")
      data = []
      for line in content:
         data.append(line.split(" "))

      arr = []

      for line in data:
         arr.append([int(line[i]) for i in range(len(line))])

      return arr
   
def isJednomasztowy(i,j,rows,cols,data):
   variants = [(1,0),(-1,0),(0,1), (0,-1)]
   isjedn = True
   for var in variants:
      next_i, next_j = i + var[0], j + var[1]

      if(0 <= next_i < rows and 0 <= next_j < cols):
         if (data[next_i][next_j] == 1):
            isjedn = False
            break
   return isjedn
   
def isDwumasztowy(i,j,rows,cols,data):
   variants = [(1,0),(-1,0),(0,1),(0,-1)]

   isDwumasztowy = False
   for var in variants:
      next_i, next_j = i + var[0], j + var[1]
   
      if(0 <= next_i < rows and 0 <= next_j < cols):
         if (data[next_i][next_j] == 1):
            isDwumasztowy = True
            break

   if(isDwumasztowy is True):
      return (next_i, next_j)
   return None

def main():
   data = get_data()
   
   rows = len(data)
   cols = len(data[0])

   dict_ships = {
      "1":[],
      "2":[]
   }

   for i in range(rows):
      for j in range(cols):
         if(i != j and abs(i - rows + 1) != j):
            continue
         
         if(data[i][j] == 0):
            continue

         if((i,j) in dict_ships.values()):
            continue

         isjedn = isJednomasztowy(i,j,rows,cols,data)
         if(isjedn is True):
            if((i,j) in dict_ships["1"]):
               continue
            dict_ships["1"].append((i,j))

         
         isDwumaszt =  isDwumasztowy(i,j,rows,cols,data)
         if(isDwumaszt is not None):
            if(isDwumaszt in dict_ships["2"]):
               continue
            dict_ships["2"].append((i,j))
            dict_ships["2"].append(isDwumaszt)

   print("jedno")
   print(dict_ships["1"])     
   print(len(dict_ships["1"]))  

   print("dwu")
   print(dict_ships["2"])     
   print(len(dict_ships["2"]) // 2)        


main()
