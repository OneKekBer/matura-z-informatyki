#https://technikprogramista.pl/kurs/zadania-maturalne-z-informatyki/lekcja/slowa-binarne-2015-pr/
def get_data():
    with open("./data.txt", "r") as f:
        content = f.read().strip().split("\n")
    return content

def get_blocks(line):
   if("0" and "1" not in line):
      return 0
   firstItem = line[0]
   l = 0
   isCorrect = True
   for r in range(1, len(line)):
      item = line[r]

      if(item == firstItem):
         continue

      if(item != firstItem):
         l = r
         while l != len(line):
            if(line[l] != item):
               isCorrect = False
               break
            
            l+=1

   if(isCorrect is True):
      return 1
   return 0

# print(get_blocks("1000011"))

def main():
   data = get_data()
   counter = 0
   for line in data:
      count = get_blocks(line)
      counter += count


   print(counter) 
      
main()