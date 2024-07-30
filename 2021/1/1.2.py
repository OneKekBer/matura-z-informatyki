def func(n):
   sqr = 1
   answ = 0
   while n > 0:
      digit = n % 10 # div
      n  = n // 10 # mod
      liczba = 9 - digit
      answ += liczba * sqr
      sqr *= 10

   return answ

print(func(732))