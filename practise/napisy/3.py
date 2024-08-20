def get_data():
   with open("./data.txt", "r") as f:
      content = f.read().strip().split("\n")

      return content

def main():
   data = get_data()
   dict = {
      "1":0,
      "0":0
   }

   for line in data:
      filter = line[0]
      isMonotoniczna = True
      for i in range(1, len(line)):
         item = line[i]

         if(item != filter):
           isMonotoniczna = False
           break
      
      if(isMonotoniczna is True):
         dict[filter] += 1
   print(dict) 
main()

