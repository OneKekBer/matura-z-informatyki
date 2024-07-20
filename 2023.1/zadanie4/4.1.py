def get_data():
   with open("./../data/brenna.txt", "r") as f:
      content = f.read().strip()[1:]
      data = content.split("\n")[1:]
      finalData = []
      for info in data:
         finalData.append(info)
      f.close()
      return finalData
      

def handleOneHour(oneHourData):
   data = oneHourData.split("\t")
   date = data[0].split()[0]
   time = data[0].split()[1]
   temperature = data[1]
   fall = data[2]
   print(time)

def list_to_float(list):
   list_float = []
   for item in list:
      floatNumber = float(item.replace(",", "."))
      list_float.append(floatNumber)
   return list_float

def find_max(list):
   max_item = -5
   for item in list:
      if(item > max_item):
         max_item = item
      
   return max_item


def find_min(list):
   min_item = 5555
   for item in list:
      if(item < min_item):
         min_item = item
      
   return min_item


def handleDayInfo(oneDayInfo):
   temperature = []
   for oneHourData in oneDayInfo:
      data = oneHourData.split("\t")
      temperature.append(data[1])
   max_item = find_max(list_to_float(temperature))
   min_item = find_min(list_to_float(temperature))
   amplitude = max_item - min_item
   return amplitude
   

data = get_data()

amplitudes = []
for i in range(len(data)):
   oneDay = data[:24]
   amplitudes.append(handleDayInfo(oneDay))
   data = data[24:]

print(find_max(amplitudes))



