#https://technikprogramista.pl/kurs/zadania-maturalne-z-informatyki/lekcja/szyfr-2012-pr/

def get_klucze():
   with open("./klucze1.txt", "r") as f:
      content = f.read().strip().split("\n")

      return content

def get_dane():
   with open("./tj.txt", "r") as f:
      content = f.read().strip().split("\n")

      return content

def get_alfabet_index(letter):
   alfabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
   index = alfabet.find(letter)
   return index + 1

# get_alfabet_index("W")

def get_hashed_word(klucz, word):
   hashed_word = ""
   klucz_index = 0

   for letter in word:
      print(letter)
      klucz_letter = klucz[klucz_index]
      # print(letter,klucz_letter)   
      ascii_summa = ord(letter) + get_alfabet_index(klucz_letter)
      # print(ascii_summa)
      if(ascii_summa > 90):
         ascii_summa = ascii_summa - 26
      
      hashed_word += chr(ascii_summa)
      klucz_index += 1

      if(klucz_index == len(klucz)):
         klucz_index = 0

   return hashed_word
# print(get_hashed_word("TOR", "MARTA"))

def main():
   klucze = get_klucze()
   dane = get_dane()
   odp = []


   for i in range(len(dane)):
      klucz = klucze[i]
      word = dane[i]

      hashed_word = get_hashed_word(klucz, word)


      odp.append(hashed_word)
   print(odp)
main()