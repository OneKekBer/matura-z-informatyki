def countingSort(arr):
   counter = [0] * 100 # or just max number for better speed
   for i in range(len(arr)):
      counter[arr[i]] += 1

   # arr = [] #if you want get reapeters
   # for i in range(len(counter)):
   #    for j in range(counter[i]):
   #       arr.append(i)
   # print(counter)

   arr = [] # without reapeters
   index = 0
   for i in counter:
      if(i == 0):
         index += 1
         continue
      arr.append(index)
      index+= 1

   return arr

# use this sort algorithm when we know range, for example from 0 to 10 
print(countingSort([1,5,4,7,1,6,8,9,4,2,2,4,6,8,2,4,7, 41, 49, 52, 23,76,3,6]))