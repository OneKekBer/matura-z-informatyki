def get_data():
   with open("./../data/pi.txt", "r") as f:
      content = f.read().strip()
      data = content.split('\n')

      f.close()   
      return data

def get_pairs(data):
   pairs = []

   while len(data) != 0:      
      firstNum = data[0]
      secondNum = data[1]

      data.pop(0)

      stringNumber = str(firstNum) + str(secondNum)
      
      pairs.append(int(stringNumber))

      if(len(data) == 1):
         break;


   return pairs


def get_arr_from_statsList(max, number):
   for pair in max:
      if(pair[0] == number):
         return pair
   return None;

def update_count_statsList(statsList, pairNumber):
   for pairArr in statsList:
      if(pairArr[0] == pairNumber):
         pairArr[1] += 1


def find_min_max_pair(statsList):
   minArr = [9999,999]
   maxArr = [0,0]
   for pairArr in statsList:
      if(pairArr[1] > maxArr[1]): # сравниваем повторение
         maxArr = pairArr
      elif(pairArr[1] < minArr[1]):
         minArr = pairArr
      continue
   print(f"MinArr: {minArr}")
   print(f"MaxArr: {maxArr}")

def get_stats(pairs):

   statsList = [[0, 0]]#число ноль было пока что ноль раз, логично
   for pairNumber in pairs:
      if(get_arr_from_statsList(statsList, pairNumber) == None):
         statsList.append([pairNumber, 1])
         continue

      update_count_statsList(statsList, pairNumber)
   find_min_max_pair(statsList)
   
      


def main():
   data = get_data()
   pairs = get_pairs(data)
   get_stats(pairs)
   # print(pairs)


main()