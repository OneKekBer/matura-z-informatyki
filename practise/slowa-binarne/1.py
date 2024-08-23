#https://technikprogramista.pl/kurs/zadania-maturalne-z-informatyki/lekcja/slowa-binarne-2015-pr/
def get_data():
    with open("./data.txt", "r") as f:
        content = f.read().strip().split("\n")
    return content

def main():
   data = get_data()
   counter = 0
   for line in data:
      count =[0,0]
      for i in range(len(line)):
         if(line[i] == "1"): 
            count[1] += 1
         else:
            count[0] += 1
      if(count[0] > count[1]):
         counter += 1
   print(counter)
      
main()