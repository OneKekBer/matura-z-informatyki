def get_data():
   with open("./data.txt", "r") as f:
      content = f.read().strip().split("\n")

      return content



def main():
   data = get_data()
   odp = []
   for line in data:
      
      jeden = 0
      zero = 0
      for i in range(len(line)):
         item = line[i]
         if(item == "1"):
            jeden+=1
         else:
            zero+=1 
         
      if(jeden == zero):
         odp.append(line)
   print(odp) 
main()

