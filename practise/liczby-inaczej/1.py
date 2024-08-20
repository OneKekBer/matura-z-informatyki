#https://technikprogramista.pl/kurs/zadania-maturalne-z-informatyki/lekcja/liczby-inaczej-2011-pr/

def get_data():
   with open("./data.txt", "r") as f:
      content = f.read().strip().split("\n")

      return content


def binary_to_number(binary):
   number = 0
   binary = binary[::-1]
   for i in range(0, len(binary)):
      bin = int(binary[i])

      if(bin == 1):
         number += 2 ** i
   return number


# print(binary_to_number("111111111111"))


def main():
   data = get_data()
   praz = 0
   for bin in data:
       number = binary_to_number(bin)

       if(number % 2 == 0):
         praz+=1
      
   print(praz)
main()