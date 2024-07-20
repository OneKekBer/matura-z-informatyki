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


print(IntToBinary(872))
print(find_block(IntToBinary(872)))