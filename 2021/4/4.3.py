def get_data():
   with open('./../data/instrukcje.txt', "r") as f:
      content = f.read().strip()
      data = content.split("\t")[0].split("\n")
      ctx = []
      for i in range(len(data)):
         ctx.append(data[i].split(" "))
      return ctx

import string
def main():
   data = get_data()
   
   list = [0] * 26

   for r in range(len(data)):
      if(data[r][0] == "DOPISZ"):
         letter = data[r][1]
         letter_index = ord(letter.lower()) - 97
         list[letter_index] += 1

   max_letter_list = max(list)
   max_letter_list_index = list.index(max_letter_list)
   max_letter = chr(max_letter_list_index + 97)
   print(max_letter, max_letter_list)



main()

#zaebis