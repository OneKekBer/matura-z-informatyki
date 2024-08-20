WAKACJE="wakacje"

def get_data():
   with open("./data/przyklad.txt", "r") as f:
      content = f.read().strip().split("\n")

      return content


def remove_with_filter(word, filter):
   answer = ""
   for i in word:
      if(i in filter):
         answer = answer + i
   return answer

def is_sequence_right(word, filterWord):
   counter = 0
   i = 0
   while True:
      if(counter == len(filterWord)):
         break;
      
      if(i == len(word)):
         break
      
      if(word[i] == filterWord[counter]):
         counter += 1
         word = word[1:]
         continue
      

      i += 1
   if(counter == len(filterWord)):
      return True
   
   return False


# word = 'urbwkcnlnngqjqrxfteaphklywflnbafazrhffewaoxxrfnzuffbqzczvwmfrzoanuevjscgmszsnjdpvxzedvnclmypujuyvypm'

# checkWord = remove_with_filter(word,WAKACJE)
# print(checkWord)
# isSequenceRight =  is_sequence_right(checkWord, WAKACJE)

# print(isSequenceRight)

def find_letter_index(word, letter):
   for i in range(0, len(word)):
      if(word[i] == letter):
         return i + 1


def get_possible_words_number(word):
   checkWord = remove_with_filter(word,WAKACJE)
   isSequenceRight =  is_sequence_right(checkWord, WAKACJE)

   if(isSequenceRight is not True):
      return 0
   
   wakacje_counter = 0
   wakacje_index = 0

   i = 0
   while i != len(word):
      letter = word[i]
      # print(wakacje_index)
      if(wakacje_index + 1 == len(WAKACJE)):
         wakacje_counter += 1
         wakacje_index = 0

      
      if(letter == WAKACJE[wakacje_index]):
         wakacje_index += 1
      
      
      i += 1
   
   return wakacje_counter

# print(get_possible_words_number("wakacje"))


# word = 'qymimoyhjphajmmwtkgmptdtskxaidarnlrddkcylwxrugykzvbcfuxajbbormwkceyhepjmoalfcincmjepagstvldstcehhoyrtaitcoblfcmmozyncuafcnxqfvxijhwguileuvkcadatkltqkvdgnwodjkeitlexiwaixxbifgpjqgfbdjkunysfycekiuqypdsxxujoscfykygjxabbpzwuittpgcwwtumqkgmgbdwvntsnzmxaswprdcffwapqqvdjxcusyottvftznxhoqujfgtbetjyrrlvpkxbwkeevctgnwutrgqagworrkssornvvdkaqlficrqqckoehjewwrfvfkakrizuwtbeudcryueiancxdtccckkcejahyymtqktdaewdruwfcnpafbcahcrzgthedllndgmzuopuhmwmnbetupgcrgiwppysvyfhurukuuhfpgcrknruqclabisdpgeirhyvwrnaozogwmbicfscmbazniccvfncftbqyqcdqgjyjqxyyugjebczpnwkiiuppbpffcwdimbgbduhbfvdsythshbflovupwdsqpfsupxqqdnssopchbaivadbnufoshgzdmubtqbarxmuktaibrpafcvzhsowgiwkcgsjmhxnkeaqafornmaalsskmjjqafjrpsqjpchbfwnzxtlynrlpzdmkruxutvxvmcxyxkouckzjnnqtsqnhblzmcmopetrmyyrwqafwzghjzasuuxfwugcrtjgfprengqpawtdekdyrgyfdaocedyjaopwpxgavrlauqaapbjbmvzuucqvdejpgiqebuiruvdapphqhvgwkgxfkabywrtldorsvdpmetmdlelzxcgdnjvkxbewxnzgvoofbfmazxplfaknedkgtpdedtwrqquoskupeslcoqbiatnmchcfgbzqnzfddzoozkcncfllntvmwronvutqqswpzlvyrwaxangrqjrrxe'
# print("odp")
# print(get_possible_words_number(word))



# def remove_duplicates(word):
#    answer = ""
   
#    for i in word:
#       if(i in answer):
#          continue
#       else:
#          answer = answer + i
         
#    return answer





def main():
   data = get_data()
   odp_arr = []
   word = "wakacjeq"
   # for word in data:
   if(len(word) < len(WAKACJE)):
      odp_arr.append(len(word))
      # continue
      return

   possible_words_count = get_possible_words_number(word)
   
   if(possible_words_count == 0):
      odp_arr.append(len(word))
      # continue
      return


   wakacje_index = 0 
   wakacje_counter = 0
   remove_letter_all = 0
   remove_letters_counter = 0

   for i in range(len(word)):
      letter = word[i]
      print(letter)
      print(remove_letters_counter)

      if(wakacje_index == len(WAKACJE)):
         wakacje_counter += 1    
         wakacje_index = 0

      print("current wakacje letter",WAKACJE[wakacje_index])
      if(letter == WAKACJE[wakacje_index]): 
         wakacje_index += 1

         remove_letter_all += remove_letters_counter
         remove_letters_counter = 0
         print("remove_letter_all", remove_letter_all)
      else:
         remove_letters_counter += 1
      
     
   
   odp_arr.append(remove_letter_all)         


   print(odp_arr)
main()