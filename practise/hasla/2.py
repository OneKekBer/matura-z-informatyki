#https://technikprogramista.pl/kurs/zadania-maturalne-z-informatyki/lekcja/hasla-2011-pp/


def get_data():
   with open("./data.txt", "r") as f:
      content = f.read().strip().split("\n")

      return content
   

def main():
   data = get_data()
   odp_arr = []
   for word in data:
      if(word == word[::-1] and len(word) % 2 == 0):
         odp_arr.append(word)
   print(odp_arr)

main()