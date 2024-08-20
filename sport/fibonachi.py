def fibo(number):
   arr = []

   for i in range(0,number + 1):
      if i > 1:
         number = arr[-1] + arr[-2]
         arr.append(number)
      else: 
         arr.append(i)

   return arr[-1]


def main():
   inp = input("enter the number")

   answer = fibo(int(inp))

   print(answer)

main()

