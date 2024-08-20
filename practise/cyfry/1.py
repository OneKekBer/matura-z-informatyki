def get_data():
   with open("./data.txt", "f") as f:
      content = f.read().strip().split("\n")

      return content
   
def main():
   data = get_data()
   parz = 0
   for number in data:
      if(number % 2 == 0):
         parz += 1 
main()