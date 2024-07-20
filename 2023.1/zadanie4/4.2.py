##helpers
import math

def find_max(list):
   max_item = -5
   for item in list:
      if(item > max_item):
         max_item = item
      
   return max_item

def list_to_float(list):
   list_float = []
   for item in list:
      floatNumber = float(item.replace(",", "."))
      list_float.append(floatNumber)
   return list_float

def find_min(list):
   min_item = 5555
   for item in list:
      if(item < min_item):
         min_item = item
      
   return min_item


def find_average(list):
   return sum(list) / len(list)


##main

def get_data():
   with open("./../data/brenna.txt", "r") as f:
      content = f.read().strip()[1:]
      data = content.split("\n")[1:]
      finalData = []
      for info in data:
         finalData.append(info)
      f.close()
      return finalData
      

dict = {"{:02}".format(i): [] for i in range(24)}


def handleOneHour(oneHourData):
   data = oneHourData.split("\t")
   date = data[0].split()[0]
   time = data[0].split()[1]
   temperature = data[1]
   fall = data[2]
   key = time.split(":")[0]
   # print(key)
   dict[key].append(temperature)




def handleDayInfo(oneDayInfo):
   for oneHourData in oneDayInfo:
      data = oneHourData.split("\t")
      handleOneHour(oneHourData)
      
  
data = get_data()

for i in range(len(data)):
   oneDay = data[:24]
   handleDayInfo(oneDay)
   data = data[24:]


keys = dict.keys()
for key in keys:

   average = find_average(list_to_float(dict[key]))
   print(f"{key}: {round(average,2)}")




