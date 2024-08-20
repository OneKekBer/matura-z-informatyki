def get_data():
   with open("./data.txt", "r") as f:
      content = f.read().strip().split("\n")

      return content
   
def main():
   data = get_data()
   min = [3123123123123, 0]
   max = [0, 0] 
   for number in data:
      summ = 0
      string = str(number)
      for i in range(0, len(str(number))):
         summ += int(string[i])

      if(min[0] > summ):
         min[0] = summ
         min[1] = number

      if(max[0] < summ): 
         max[0] = summ
         max[1] = number

   print(min, max)


main()