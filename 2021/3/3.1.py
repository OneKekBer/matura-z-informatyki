def func(n):
   if n > 0:
      print(n)
      func(n - 2)
      print("pracuje")
      print(n)

func(8)