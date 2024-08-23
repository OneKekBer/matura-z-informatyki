#https://technikprogramista.pl/kurs/zadania-maturalne-z-informatyki/lekcja/wlasnosci-liczb-2020-pr
#https://arkusze.pl/maturalne/informatyka-2020-czerwiec-matura-stara-rozszerzona-2.pdf


def get_data():
    with open("./przyklad.txt", "r") as f:
        content = f.read().strip().split("\n")
    return content


def num_to_arr(num):
   string = str(num)
   arr = []
   for i in range(len(string)):
      letter = string[i]
      if(int(letter) not in arr):
         arr.append(int(letter))
   arr.sort()
   return arr


def is_number_contains_all_digits_form_array(num, arr):
   
   string = str(num)
   new_arr = num_to_arr(string)
   if(new_arr != arr):
      return False
   return True
      
def main():
   data = get_data()
   odp_arr = []
   counter = 0
   for i in range(len(data)):
      current_number = int(data[i])
      current_arr = num_to_arr(current_number)
      for j in range(i + 1, len(data)):
        
         
         if is_number_contains_all_digits_form_array(data[j], current_arr) is True:
            new_odp = [current_number, int(data[j])]
            new_odp.sort()

            if(new_odp not in odp_arr):
            
               odp_arr.append(new_odp)

   print(odp_arr)
   print(len(odp_arr))





main()