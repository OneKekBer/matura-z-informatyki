def isNumberPrime(num):
   #число которое делиться на себя и 1
   if num > 1:
      for i in range(2, num // 2 + 1):
         if(num % i == 0):
            return False
      return True
   return False

def GeneratePrimeNumbers(min, max):
   list = []
   for i in range(min, max):
      if(isNumberPrime(i)):
         list.append(i)

   return list

