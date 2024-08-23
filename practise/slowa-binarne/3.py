#https://technikprogramista.pl/kurs/zadania-maturalne-z-informatyki/lekcja/slowa-binarne-2015-pr/
def get_data():
    with open("./data.txt", "r") as f:
        content = f.read().strip().split("\n")
    return content

def count_zeros(line):
   if("1" not in line):
      return [line, len(line)]
   if("0" not in line):
      return [line, 0]

   max_zero = 0
   count_zero = 0

   for i in range(len(line)):
      item = line[i]
      if(item == "0"):
         count_zero += 1
         continue

      if(item == "1"):
         max_zero = max(max_zero,count_zero)
         count_zero = 0
      continue
   max_zero = max(max_zero,count_zero)
   return [line, max_zero]
   

def main():
   data = get_data()
   counter = 0
   max_zero = 0
   good_arrs = []
   for line in data:
      get_max_zeros = count_zeros(line)
      if(max_zero == get_max_zeros[1]):
         good_arrs.append(get_max_zeros[0])
      elif(max_zero < get_max_zeros[1]):
         max_zero = get_max_zeros[1]
         good_arrs = []
         good_arrs.append(get_max_zeros[0])

      
   print(max_zero,good_arrs) 
      
main()