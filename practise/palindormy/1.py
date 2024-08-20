#https://technikprogramista.pl/kurs/zadania-maturalne-z-informatyki/lekcja/palindromy-2010-pp/

def get_data():
   with open('./data.txt') as f:
      content = f.read().strip().split('\n')

      return content

def reverse_word(word):
   new_word = ""
   for i in range(0, len(word)):
      new_word = word[i] + new_word
   return new_word

def main():
   data = get_data()
   odp_arr = []
   for word in data:
      if(len(word) % 2 != 0):
         continue
      
      reversed_word  = reverse_word(word)
      if(reversed_word == word):
         odp_arr.append(word)
          
   print(odp_arr)

   # print(data)

main()