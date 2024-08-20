def get_data():
   with open("./data/slowa.txt", "r") as f:
      content = f.read().strip().split("\n")

      return content


def main():
   data = get_data()
   odp_arr = []
   for word in data:
      dict = {
         "w":0,
         "a":0,
         "k":0,
         "c":0,
         "j":0,
         "e":0,
      }
      for i in range(0, len(word)):
         letter = word[i]
         if(letter in dict.keys()):
            dict[letter] += 1

      dict["a"] = dict["a"] // 2
      print(dict)
      dict_arr = list(dict.values())

      min_val = min(dict_arr)
      odp_arr.append(min_val)

   print(odp_arr)
main()