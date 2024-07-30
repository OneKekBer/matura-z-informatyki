def find3MaxIncreasingNumbers(list, k):
   list.sort()
   # print(list)
   return list[k + 1:]


print(find3MaxIncreasingNumbers([4,6,1,7,8,9,4,12,6,65,1], 5))