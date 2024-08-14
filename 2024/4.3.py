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
   
def checkIsOneTitleShip(i,j,rows,cols,data):
   variants = [(1,0), (-1,0),(0,1), (0,-1)]
   for var in variants:
            next_i, next_j = i + var[0], j + var[1]
            if(0 <= next_i < rows and 0 <= next_j < cols):
               if (data[next_i][next_j] == 1):
                  return False
   return True
   
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
   counter = 0

   print()

   rows = len(data)
   cols = len(data[0])

   dwumasztowce = []

   for i in range(rows):
      for j in range(cols):
         if(data[i][j] == 0):
            continue

         if((i,j) in dwumasztowce):
            continue

         
         isDwumaszt =  isDwumasztowy(i,j,rows,cols,data)
         if(isDwumaszt is not None):
            dwumasztowce.append((i,j))
            dwumasztowce.append(isDwumaszt)
            

   print(len(dwumasztowce) // 2)
   print(dwumasztowce)
main()
