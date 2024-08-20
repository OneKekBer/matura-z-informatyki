def count_distance(x1, y1, x2, y2):
   x_dist = abs(x1 - x2)
   y_dist = abs(y1 - y2)

   return x_dist + y_dist


def main():
   x1, y1 = input("enter start coords: ").split()
   x2, y2 = input("enter end coords: ").split()

   distance = count_distance(int(x1), int(y1), int(x2), int(y2))

   print("distance:", distance)

main()