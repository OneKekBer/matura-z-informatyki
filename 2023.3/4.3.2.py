WAKACJE="wakacje"

def get_data():
   with open("./data/slowa.txt", "r") as f:
      content = f.read().strip().split("\n")

      return content
   

   
def get_possible_count(word):
   if(len(word) < len(WAKACJE)):
      return 0
   
   index = 0
   wakacje_counter = 0 # сколько слов wakacje

   for i in range(len(word)):
      letter = word[i]

      if(letter == WAKACJE[index]):
         index += 1

      if(index == len(WAKACJE)):
         wakacje_counter += 1
         index = 0

   return wakacje_counter

# ewe = get_possible_count("wa")
# print(ewe)
def get_count_remove_items(word):
   index = 0
   index_summ = 0

   remove_counter = 0
   remove_sum = 0


   for i in range(len(word)):
      print("----")
      letter = word[i]

      
      if(index == len(WAKACJE)):
         index_summ += 1
         index = 0

      if(letter == WAKACJE[index]):
         index += 1

         
         remove_sum += remove_counter
         remove_counter = 0 
      else:
         remove_counter += 1
      
   
   remove_sum += remove_counter

   return remove_sum

# word = "llllwakacjlllwakacjele"
# print(get_count_remove_items(word))

def main():
   data = get_data()
   odp_data =[]
   for word in data:
      possible_count = get_possible_count(word)

      if(possible_count == 0):
         odp_data.append(len(word))
         continue

      count_remove_items = len(word) -  (possible_count * len(WAKACJE))

      odp_data.append(count_remove_items)

   print(odp_data)

main()



