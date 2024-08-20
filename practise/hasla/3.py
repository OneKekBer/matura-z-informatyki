#https://technikprogramista.pl/kurs/zadania-maturalne-z-informatyki/lekcja/hasla-2011-pp/


def get_data():
   with open("./data.txt", "r") as f:
      content = f.read().strip().split("\n")

      return content
   

def main():
   data = get_data()
   odp_arr = []
   for word in data:
      for i in range(0, len(word)):
         if(i == len(word) - 1):
            break
         
         if(ord(word[i]) + ord(word[i+1]) == 220):
            if(word not in odp_arr):
               odp_arr.append(word)
         
   print(odp_arr)

main()