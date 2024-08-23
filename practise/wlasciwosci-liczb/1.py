#https://technikprogramista.pl/kurs/zadania-maturalne-z-informatyki/lekcja/wlasnosci-liczb-2020-pr
#https://arkusze.pl/maturalne/informatyka-2020-czerwiec-matura-stara-rozszerzona-2.pdf


def get_data():
    with open("./przyklad.txt", "r") as f:
        content = f.read().strip().split("\n")
    return content


def is_prime_number(x):
   x = int(x)
   if(x > 1):
      for i in range(2, x // 2 + 1):
         if(x % i == 0):
            return False
      return True
   return False


def main():
   data = get_data()
   min_num = 32131231231231231231321
   max_num = 0
   counter = 0
   for number in data:

      if(is_prime_number(number) is True):
         counter += 1
         number = int(number)
         if(number > max_num): max_num = number
         if(min_num > number): min_num = number
   print(min_num, max_num, counter)


main()