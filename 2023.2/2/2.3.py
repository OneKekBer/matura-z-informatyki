def get_data():
   with open('./../data/bin_przyklad.txt') as f:
      content = f.read().strip()
      data = content.split('\n')
      return data

def BinaryToInt(binaryValue):
    intValue = 0
    length = len(binaryValue)

    for i in range(length):
        bit = int(binaryValue[length - i - 1])
        intValue += bit * (2 ** i)
    
    return intValue

def main():
   data = get_data()
   
   correctData = [0, '000']
   
   for line in data:
      # print(line)   
      lineInt = BinaryToInt(line)
      if(correctData[0] < lineInt):
         correctData[0] = lineInt;
         correctData[1] = line;
         
   
   print(correctData[1])


main();