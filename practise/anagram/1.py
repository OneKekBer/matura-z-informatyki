#https://technikprogramista.pl/kurs/zadania-maturalne-z-informatyki/lekcja/anagram-2010-pr/


def get_data():
   with open("./data.txt", "r") as f:
      content = f.read().strip().split("\n")

      data = [content[i].split(' ') for i in range(len(content))]

      return data
   

def main():
   data = get_data()
   odp_arr = []
   for array in data:

      current_length = len(array[0])
      isLengthCorrect = True
      for i in range(1, len(array)):
         if(len(array[i]) != current_length ):
            isLengthCorrect = False
            break
      

      if(isLengthCorrect is True):
         odp_arr.append(array)

   print(odp_arr)

main()