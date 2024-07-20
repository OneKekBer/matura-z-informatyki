def get_data():
   with open('./../data/bin.txt') as f:
      content = f.read().strip()
      data = content.split('\n')
      return data
   
def find_block(binaryCode):
   block = 0

   for i in range(len(binaryCode)):
      if(i == 0):
         block += 1
         continue 

      if(binaryCode[i ] != binaryCode[i - 1]):
         block += 1
         continue
      
   return block;


def main():
   data = get_data()
   
   allCorrectLines = 0
   for line in data:
      if(find_block(line) <= 2):
         allCorrectLines += 1
   
   print(allCorrectLines)


main();