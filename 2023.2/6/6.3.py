def get_data():
   with open("./../data/owoce.txt", "r") as f:
      content = f.read().strip().split("\n")

      data = [content[i].split("\t") for i in range(len(content))]

      return data[1:]
   

def find_good_key(jam, maxKey, avgKey):
   good_key = ""
   for key in jam:
      print(key)
      key_arr = key.split("-")
      if(avgKey in key_arr and maxKey in key_arr):
         good_key = key
   return good_key

def main():
   data = get_data()

   magazyn = {
      "maliny":0,
      "truskawki":0,
      "porzeczki":0
   }

   jam = {
      "maliny-truskawki":0,
      "maliny-porzeczki":0,
      "truskawki-porzeczki":0,
   }

   for line in data:
      maliny = int(line[1])
      truskawki = int(line[2])
      porzeczki = int(line[3])

      magazyn["maliny"] += maliny
      magazyn["truskawki"] += truskawki
      magazyn["porzeczki"] += porzeczki
            
      magazyn = dict(sorted(magazyn.items(), key=lambda x:x[1], reverse=True))

      avgKey = list(magazyn.keys())[1]
      maxKey = list(magazyn.keys())[0]

      good_key = find_good_key(jam, maxKey, avgKey)

      print(good_key)
      if(good_key in jam):
         magazyn[maxKey] -= magazyn[avgKey]
         magazyn[avgKey] = 0

         jam[good_key] += 1

   print(jam)
main()