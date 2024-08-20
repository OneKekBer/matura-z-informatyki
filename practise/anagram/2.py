#https://technikprogramista.pl/kurs/zadania-maturalne-z-informatyki/lekcja/anagram-2010-pr/


def get_data():
   with open("./data.txt", "r") as f:
      content = f.read().strip().split("\n")

      data = [content[i].split(' ') for i in range(len(content))]

      return data
   
def isCorrectLength(array):
   current_length = len(array[0])
   isLengthCorrect = True
   for i in range(1, len(array)):
      if(len(array[i]) != current_length ):
         isLengthCorrect = False
         break
   
   if(isLengthCorrect is True):
      return True
   return False

def main():
   data = get_data()
   odp_arr = []
   for array in data:

      is_length_correct = isCorrectLength(array)

      if(is_length_correct is False):
         continue

      isArrCorrect = True
      for i in range(1, len(array)):
         word = array[i]
         mainWord = array[0]

         for j in range(0, len(word)):
            letter = word[j]
            if(letter in mainWord):
               mainWord = mainWord.replace(letter, "")
            else:
               isArrCorrect = False
               break
         
      if(isArrCorrect is True):
         odp_arr.append(array)
      
   print(odp_arr)

main()
