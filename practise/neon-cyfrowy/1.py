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

# print(get_next_alfabet_letter(""))

def main():
   data = get_data()
   word = ''
   for item in data:
      instrukcja = item.split(" ")[0] 
      letter = item.split(" ")[1]
      match instrukcja:
         case "DOPISZ":
            word = word + letter
         case "ZMIEN":
          
            word = word[:-1]
            word = word + letter
          
            
         case "USUN":
            word = word[:-1]
         case "PRZESUN":
            next_letter = get_next_alfabet_letter(letter)
            word = word.replace(letter, next_letter, 1)
         
   print(word)

main()   