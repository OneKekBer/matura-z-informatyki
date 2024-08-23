#https://technikprogramista.pl/kurs/zadania-maturalne-z-informatyki/lekcja/ciekawe-napisy-2014-pr/

def get_data():
    with open("./data.txt", "r") as f:
        content = f.read().strip().split("\n")
    return content

def main():
   data = get_data()
   odp = []
   buffer_array = []
   for line in data:
      
      if(line in odp):
         continue
      
      if(line in buffer_array):
         buffer_array.remove(line)
         odp.append(line)
         continue

      buffer_array.append(line)

   print(odp)

main()