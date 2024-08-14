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
   
def main():
   data = get_data()
   variants = [(1,0), (-1,0),(0,1), (0,-1), (1,1), (1,-1), (-1, 1), (-1,-1)]
   counter = 0

   print()

   rows = len(data)
   cols = len(data[0])

   for i in range(rows):
      for j in range(cols):
         if(data[i][j] == 1):
            continue
         
         isShipNear = False

         for var in variants:
            next_i, next_j = i + var[0], j + var[1]
            
            if(0 <= next_i < rows and 0 <= next_j < cols):
               if (data[next_i][next_j] == 1):
                  isShipNear = True
                  break

         if(isShipNear is not True):
            counter += 1
         
   print(counter)
main()
