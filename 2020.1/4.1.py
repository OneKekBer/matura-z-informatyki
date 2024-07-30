def isNumberPrime(num):
   #число которое делиться на себя и 1
   if num > 1:
      for i in range(2, num//2 + 1):
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


primeNumbers = GeneratePrimeNumbers(1,1000)
# print(primeNumbers)

def FinSumNumbers(num):
   num = int(num)
   if num <= 4:
      return
   
   if(num % 2 != 0):
      return
   
   l = 0
   r = len(primeNumbers) - 1
   for l in range(len(primeNumbers)):

      while r > 0:
         if(primeNumbers[l] + primeNumbers[r] == num):
            return [num, primeNumbers[l], primeNumbers[r]]
         r-= 1
      r = len(primeNumbers) - 1
      
      
   return


# print(FinSumNumbers("15"))
def get_data():
   with open("./data/pary.txt", "r") as f:
      content = f.read().split("\n")
      data = [content[i].split(" ") for i in range(len(content))]
      return data

# print(FinSumNumbers(562))
data = get_data();

for line in data:
   if(line == ['']):
      continue
   number = line[0]
   answ = FinSumNumbers(number)
   if(answ != None):
      print(answ)