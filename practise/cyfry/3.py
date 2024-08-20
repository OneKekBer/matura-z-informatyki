def get_data():
   with open("./data.txt", "r") as f:
      content = f.read().strip().split("\n")

      return content
   
def main():
   data = get_data()
   odp = []
   for number in data:
      isUpping = True
      summ = 0
      string = str(number)
      for i in range(0, len(string)):
         num = int(string[i])

         if(i == len(string) - 1):
            continue

         if(num < int(string[i + 1])):
            continue
         else:
            isUpping = False
            break
      if(isUpping is False):
         continue
      odp.append(number)
      
   print(odp)         




main()