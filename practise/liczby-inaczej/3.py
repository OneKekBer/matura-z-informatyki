
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

def number_to_binary(number):
    binary_representation = bin(number)[2:]  # Convert to binary and remove the '0b' prefix
    return binary_representation

# number_to_binary(5)

# print(binary_to_number("111111111111"))


def main():
   data = get_data()
   summ = 0
   for bin in data:
      number = binary_to_number(bin)

      if(len(bin) == 9 ):
         summ+= number
      
   bin_summ = number_to_binary(summ)

   print(bin_summ)
main()