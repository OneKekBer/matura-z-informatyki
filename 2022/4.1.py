def get_data():
   with open("./data/liczby.txt", "r") as f:
      content = f.read().strip().split("\n")

      return content
   
def main():
   data = get_data()

   odp_counter = 0

   first = -1
   for number in data:
      strNumber = str(number)


      if(int(strNumber[0]) == int(strNumber[-1])):
         if(first == -1):
            first = number
         odp_counter +=1

   print(odp_counter)
   print(first)

main()