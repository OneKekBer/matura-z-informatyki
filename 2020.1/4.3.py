def get_data():
   with open("./data/pary.txt", "r") as f:
      content = f.read().split("\n")
      f.close()
      data = [content[i].split(" ") for i in range(len(content))]
      return data



def remove_duplicates(string):
   correctString = ""

   for char in string:
      if(char in correctString):
         continue
      else:
         correctString += char
   return correctString




def get_porzadek(string):
   correctString = remove_duplicates(string)
   alfabet = "abcdefghijklmnopqrstuvwxyz"

   counter = 0
   for i in range(len(correctString)):
      if(correctString[i] == alfabet[i]):
         counter += 1
      else:
         break
   return counter



def get_min(arr):
   minItem = [20000, "abcdefghijklmnopqrstuvwxyz"]
   for i in range(len(arr)):
      currentItem = arr[i]

      if(minItem == []):
         minItem = currentItem
         continue

      if(int(minItem[0]) > int(currentItem[0])):
         minItem = currentItem
      
      if(int(minItem[0]) == int(currentItem[0]) and get_porzadek(minItem[1]) < get_porzadek(currentItem[1])):
         minItem = currentItem

   return minItem
      



def main():
   data = get_data()
   filteredLines = []
   for line in data:
      if(line == [""]):
         continue
      if(int(line[0]) == len(line[1])):
         filteredLines.append(line)
   print(get_min(filteredLines))

main();

#dostalbym 3 pkt, nie rozumie dla czego,