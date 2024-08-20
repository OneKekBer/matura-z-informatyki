#https://technikprogramista.pl/kurs/zadania-maturalne-z-informatyki/lekcja/liczby-2013-pr/

def get_data():
    with open("./data.txt", "r") as f:
        content = f.read().strip().split("\n")
    return content

def main():
   data = get_data()
   counter = 0
   for line in data:
      if(line[0] == line[-1]): counter += 1 
   print(counter)
      
       

main()