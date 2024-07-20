def get_data():
   with open('./../data/bin.txt') as f:
      content = f.read().strip()
      data = content.split('\n')
      return data


def IntToBinary(val, binaryValue = ""):
   if(val == 0):
      return binaryValue
   else:
      if(val % 2 == 1):
         binaryValue = "1" + binaryValue
      else: binaryValue = "0" + binaryValue

      val = val // 2

      return IntToBinary(val, binaryValue)



def BinaryToInt(binaryValue):
    intValue = 0
    length = len(binaryValue)

    for i in range(length):
        bit = int(binaryValue[length - i - 1])
        intValue += bit * (2 ** i)
    
    return intValue




def main():
   data = get_data()

   content = ""
   for line in data:
      number = BinaryToInt(line)
      halfNumber = number // 2

      answ = number ^ halfNumber
      binaryAnswer = IntToBinary(answ)
      content += binaryAnswer + "\n"

      f = open("./odpowiedz_2.5.txt", "w")

      f.write(content) 
   
   print(content)




main()