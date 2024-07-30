def get_data():
   with open("./data/pary.txt", "r") as f:
      content = f.read().split("\n")
      f.close()
      data = [content[i].split(" ") for i in range(len(content))]
      return data


def count_string(text):
   maxString = ""
   currentString = ""
   for r in range(len(text)):
      currentLetter = text[r]

      if len(currentString) == 0:
         currentString += currentLetter
         continue

      if(currentString[-1] == currentLetter):
         currentString += currentLetter
      else:
         if(len(currentString) > len(maxString)):
            maxString = currentString
         currentString = currentLetter
         continue
      if(len(currentString) > len(maxString)):
         maxString = currentString
   return(maxString)


def write_answ(answs):
   with open('4.2.txt', '+w') as f:
      for answ in answs:
         if(answ == ""):
            continue
         f.write(f'{answ} {len(answ)}\n')

def main():
   data = get_data()
   answ = []
   for line in data:
      if(line == [""]):
         continue
      answ.append(count_string(line[1]))
   write_answ(answ)
   
main();

