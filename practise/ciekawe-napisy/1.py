#https://technikprogramista.pl/kurs/zadania-maturalne-z-informatyki/lekcja/ciekawe-napisy-2014-pr/

def get_data():
    with open("./data.txt", "r") as f:
        content = f.read().strip().split("\n")
    return content


def is_number_prime(number):
   if number > 1:
       for i in range(2,number // 2 + 1):
           if(number % i == 0):
               return False
       return True
   return False



def main():
   data = get_data()
   odp = 0
   for line in data:
      ascii_summa = 0
      for i in range(len(line)):
           ascii_summa += ord(line[i])

      if(is_number_prime(ascii_summa) is True):
          odp+= 1

   print(odp)

main()