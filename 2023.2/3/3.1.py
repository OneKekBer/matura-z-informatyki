def get_data():
   with open("./../data/pi.txt") as f:
      content = f.read().strip()
      data = content.split('\n')

      return data




def main():
   data = get_data()
   counter = 0;

   while len(data) != 0:
      
      firstNum = data[0]
      secondNum = data[1]

      data.pop(0)

      stringNumber = str(firstNum) + str(secondNum)
      # print(stringNumber)
      if(int(stringNumber) > 90):
         counter += 1

      if(len(data) == 1):
         break;

       

   print(counter)


#zaebis
main()