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
   

def count_pairs(cache):
   print(cache)
   visited = set()

   pairs = 0
   for i in range(0, len(cache)):
      for j in range(i + 1, len(cache)):
         rootCoords = cache[i]
         if rootCoords in visited:
            continue
         
         jCoords = cache[j]
         if(rootCoords[0] == jCoords[1] and rootCoords[1] == jCoords[0]):
            print(rootCoords, jCoords)
            pairs += 1
            visited.add(rootCoords)
            visited.add(jCoords)
            

   return pairs

# print(count_pairs([(4, 18), (18, 4), (5,4), (5,5), (4,5)]))



def checkIsOneTitleShip(i,j,rows,cols,data):
   variants = [(1,0), (-1,0),(0,1), (0,-1)]
   for var in variants:
            next_i, next_j = i + var[0], j + var[1]
            if(0 <= next_i < rows and 0 <= next_j < cols):
               if (data[next_i][next_j] == 1):
                  return False
   return True


def main():
   data = get_data()

   rows = len(data)
   cols = len(data[0])

   print(rows)
   cache = []  
   pairs = 0
   for i in range(rows):
      for j in range(cols):
         if( i != j):
            continue
         
         k = i
         l = j
         while k != 0:
            if(data[k][j] == 1):
               if checkIsOneTitleShip(k,j,rows,cols, data) is True and k != j:
                  cache.append((k,j))
            k-= 1

         while l != 0:
            if(data[i][l] == 1):
               if checkIsOneTitleShip(i,l,rows,cols, data) is True and i != l:
                  cache.append((i,l))
            l-= 1

         pairs += count_pairs(cache)
         print(cache)
         cache = []
   print(pairs)
main()
