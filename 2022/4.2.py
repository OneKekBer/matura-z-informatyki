def get_data():
   with open("./data/liczby.txt", "r") as f:
      content = f.read().strip().split("\n")

      return content

def is_prime_number(num):
   if num > 1:
      for i in range(2, num // 2 + 1):
         if(num % i == 0):
            return False
      return True
   return False   


def get_prime_numbers(min, max):
   odp = []
   for i in range(min, max):
      if(is_prime_number(i)):
         odp.append(i)
   return odp


def remove_duplicates(arr):
   odp = []

   for i in arr:
      if(i in odp):
         continue
      odp.append(i)

   return odp



def find_prime_dividers_of_number(num, prime_numbers):
   odp = []

   index = 0
   while num > 1:
      if(num % prime_numbers[index] == 0):

         num = num // prime_numbers[index]
         odp.append(prime_numbers[index])
         index = 0   
         continue
      
      index += 1
         
   return odp


# prime_numbers = get_prime_numbers(2, 100)
# print(find_prime_dividers_of_number(2100, prime_numbers))

def main():
   data = get_data()
   prime_numbers = get_prime_numbers(2, 100000)
   maxNumber = 0
   maxCzynniki = []

   maxDiffrentNumber = 0
   maxDiffrentCzynniki = []

   for number in data:
      number = int(number)
      dividers = find_prime_dividers_of_number(number, prime_numbers)
      if(len(maxCzynniki) < len(dividers)):
         maxCzynniki = dividers
         maxNumber = number
      
      if(len(maxDiffrentCzynniki) < len(remove_duplicates(dividers))):
         maxDiffrentNumber = number
         maxDiffrentCzynniki = remove_duplicates(dividers)

   
   print("max number: ", maxNumber)
   print("maxCzynniki length: ", len(maxCzynniki))
   
   
   print("max diffrent: ", maxDiffrentNumber)
   print("max diffrent length: ", len(maxDiffrentCzynniki))
   

   
main()