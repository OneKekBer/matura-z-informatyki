#https://technikprogramista.pl/kurs/zadania-maturalne-z-informatyki/lekcja/wlasnosci-liczb-2020-pr
#https://arkusze.pl/maturalne/informatyka-2020-czerwiec-matura-stara-rozszerzona-2.pdf


def get_data():
    with open("./przyklad.txt", "r") as f:
        content = f.read().strip().split("\n")
    return content


def int_to_bin(x):
   x = int(x)

   binary = bin(x)
   return binary[2:]

def is_prawie_palindrom(binary):
   i = 0 
   while i != 10:
      binary = "0" + binary
      if(binary == binary[::-1]):
         return True
      i += 1
   return False

# print(is_prawie_palindrom("110"))

def main():
   data = get_data()

   counter = 0
   for number in data:
      binary = int_to_bin(number)

      if(binary == binary[::-1]):
         print(binary, len(binary))
         counter += 1
         continue
      elif is_prawie_palindrom(binary) is True:
         print(binary, len(binary))
         counter += 1

   print(counter)

         


main()