def get_data():
   with open("./data/slowa.txt", "r") as f:
      content = f.read().strip().split("\n")

      return content

def main():
   data = get_data()
   odp_arr = []
   for word in data:
      dict = {
         "k":0,
         "w":0
      }
      for i in range(0, len(word)):
         letter = word[i]
         if(letter in dict.keys()):
            dict[letter] += 1

      if(list(dict.values())[0] == list(dict.values())[1]):
         odp_arr.append(word)
   for i in odp_arr:
      print(i)
main()