def get_data():
   with open("./data.txt", "r") as f:
      content = f.read().strip().split("\n")

      return content



def main():
   data = get_data()
   parz = 0
   for line in data:
      if(len(line) % 2 == 0):parz += 1
   print(parz) 
main()

