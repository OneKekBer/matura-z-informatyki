def get_data():
    with open("./przyklad.txt", "r") as f:
        content = f.read().strip().split("\n")
    return content


def get_next_alfabet_letter(letter):
   alfabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
   letter.upper() 
   for i in range(1, len(alfabet)):
      if(letter == alfabet[i]):
         if(i == len(alfabet) - 1):
            return "A"
         return alfabet[i+1]

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
            print(word)
            word = word[:-1]
            word = word + letter
            print(word)
            
         case "USUN":
            word = word[:-1]
         case "PRZESUN":
            next_letter = get_next_alfabet_letter(letter)
            word = word.replace(letter, next_letter, 1)
         
   print(len(word))

main()