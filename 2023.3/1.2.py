


def Function(arr, len):
   currentNumber = 0
   length = 0

   for i in range(0,len):
      item = arr[i]
      if(item == 0):
         currentNumber = item
         continue

      if(currentNumber == item):
         continue
      
      if(i == len and currentNumber != item):
         length += 2
         break

      if(currentNumber != item):
         currentNumber = item
         length += 2

   return length


arr = [1,1,1,1,4]
print(Function(arr, len(arr)))