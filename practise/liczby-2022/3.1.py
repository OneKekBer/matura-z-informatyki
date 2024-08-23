def get_data():
   with open("./data.txt", "r") as f:
      content = f.read().strip().split("\n")
      data = [int(content[i]) for i in range(len(content))]
      data.sort()
      return data

def czy_dobra_trojka(x,y,z):
   if(y % x == 0 and z % y == 0):
      return True
   return False

def czy_dobra_piatka(x,y,z,u,w):
   if(y % x == 0 and z % y == 0 and u % z == 0 and w % u == 0):
      return True
   return False

def find_trojki(array):
   odp = []
   n = len(array)
   for i in range(n):

      for j in range(i+1, n):
         if(array[j] % array[i] != 0):
            continue
         for k in range(j + 1, n):
            if(array[k] % array[j] != 0):
               continue

            if czy_dobra_trojka(array[i], array[j],array[k]) is True:
               odp.append([array[i], array[j],array[k]])
   return odp

def find_piatki(array):
   odp = []
   n = len(array)
   for i in range(n):
      for j in range(i+1, n):
         if(array[j] % array[i] != 0):
            continue
         
         for k in range(j + 1, n):
            if(array[k] % array[j] != 0):
               continue

            for l in range(k+1,n):
               if(array[l] % array[k] != 0):
                  continue

               for m in range(l+1,n):
                  if(array[m] % array[l] != 0):
                     continue

                  if czy_dobra_piatka(array[i], array[j], array[k], array[l], array[m]) is True:
                     odp.append([array[i], array[j], array[k],array[l], array[m]])
   return odp



def main():
   data = get_data()
   # print(data)
   trojki = find_trojki(data)

   print("trojki: ",trojki)
   print("trojki length : ",len(trojki))


   piatki = find_piatki(data)
   
   print("piatki: ",piatki)
   print("piatki length : ",len(piatki))

main()