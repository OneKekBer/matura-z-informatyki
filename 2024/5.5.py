
import math
def get_data():
   with open('./data/jablka.txt', "r") as f:
      content = f.read().strip().split("\n")
      data = [content[i].split("\t") for i in range(len(content))]
      return data
   
def main():
   data = get_data()

   skidos_counter = 0
   skidos_all = 0

   dict_user = {}

   for line in data:
      user = line[3]
      kilo = int(line[4])

      if(user in dict_user):
         dict_user[user][0] += kilo
         currentUserKilo = dict_user[user][0] 
      
         if(currentUserKilo > 15000 and currentUserKilo < 20000 and dict_user[user][1] is True):
            skidos_all +=  kilo * 0.05
            skidos_counter += 1
            dict_user[user][1] == False

         if(currentUserKilo > 20000 and dict_user[user][2] is True):
            skidos_all +=  kilo * 0.1
            skidos_counter += 1
            dict_user[user][2] == False

      else:
         dict_user[user] =  [kilo, True, True]
   print(round(skidos_counter, 2))
   print(skidos_all)



main()