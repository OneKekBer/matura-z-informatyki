#https://technikprogramista.pl/kurs/zadania-maturalne-z-informatyki/lekcja/ciekawe-napisy-2014-pr/

def get_data():
    with open("./data.txt", "r") as f:
        content = f.read().strip().split("\n")
    return content

def main():
   data = get_data()
   odp = []
   for line in data:
      isRosnacy = True
      
      for i in range(len(line)):
         if(i == len(line) - 1):
             continue
         
         if(ord(line[i]) >= ord(line[i + 1])):
            isRosnacy = False

      if(isRosnacy is True):
          odp.append(line)

   print(odp)

main()