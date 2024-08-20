def get_data():
   with open("./data.txt", "r") as f:
      content = f.read().strip().split("\n")

      return content

def main():
   k = [2,17]
   dict = {}
   for i in range(k[0], k[1]):
      dict[str(i)] = 0
   print(dict)
   data = get_data()
   

   for line in data:
      length = len(line)
      dict[str(length)] += 1
   print(dict) 
main()

