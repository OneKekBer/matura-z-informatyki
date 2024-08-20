#https://technikprogramista.pl/kurs/zadania-maturalne-z-informatyki/lekcja/hasla-2011-pp/


def get_data():
   with open("./data.txt", "r") as f:
      content = f.read().strip().split("\n")

      return content
   

def main():
   data = get_data()
   parz = 0
   nie_parz = 0
   for word in data:
      if(len(word) % 2 == 0):
         parz+= 1
      else:
         nie_parz += 1
   print(parz,nie_parz)

main()