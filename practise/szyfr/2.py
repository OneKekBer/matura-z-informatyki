#https://technikprogramista.pl/kurs/zadania-maturalne-z-informatyki/lekcja/szyfr-2012-pr/

def get_klucze():
   with open("./klucze2.txt", "r") as f:
      content = f.read().strip().split("\n")

      return content

def get_dane():
   with open("./sz.txt", "r") as f:
      content = f.read().strip().split("\n")

      return content

def get_alfabet_index(letter):
   alfabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
   index = alfabet.find(letter)
   return index + 1


def get_hashed_word(klucz, word):
   original_word = ""
   klucz_index = 0

   for letter in word:
      klucz_letter = klucz[klucz_index]
      # print(letter, klucz_letter)
      ascii_summa = ord(letter) - get_alfabet_index(klucz_letter)
      # print(ord(letter) - get_alfabet_index(klucz_letter))

      if(ascii_summa < 65):
         ascii_summa = ascii_summa + 26
      
      original_word += chr(ascii_summa)
      klucz_index += 1

      if(klucz_index == len(klucz)):
         klucz_index = 0

   return original_word

# print(get_hashed_word("WODA", "IPXP"))


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