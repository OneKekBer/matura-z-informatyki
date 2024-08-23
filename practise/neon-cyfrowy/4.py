def get_data():
    with open("./instrukcje.txt", "r") as f:
        content = f.read().strip().split("\n")
    return content


def get_next_alfabet_letter(letter):
   alfabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
   letter.upper() 
   for i in range(0, len(alfabet)):
      if(letter == alfabet[i]):
         if(i == len(alfabet) - 1):
            return "A"
         return alfabet[i+1]
      



def main():
   data = get_data()
   letters_dict = {}
   
   for item in data:
      instruction = item.split(" ")[0]
      letter = item.split(" ")[1]
      if(instruction != "DOPISZ"):
         continue
      # print(instruction)
      
      if(letter not in letters_dict):
         letters_dict[letter] = 1
      else:
         letters_dict[letter] += 1

   sorted_items = sorted(letters_dict.items(), key=lambda item: item[1], reverse=True)
   print(sorted_items[0])

main()   