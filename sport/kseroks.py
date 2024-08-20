# 22 str


def main():
   n, k = input("enter n and k: ").split()
   
   n = int(n)
   k = int(k)

   i = n // k # ищем ближайшие этажи

   if i == 0: # нулевого этажа нет!!!
      i = 1
   

   lower = i * k # нижний этаж
   upper = (i + 1) * k

   lower_distance = abs(n - lower) #расстояние от нижнего этажа до нашего
   upper_distance = abs(n - upper) 

   print(min(lower_distance, upper_distance))


   # print(lower_distance, upper_distance)

main()