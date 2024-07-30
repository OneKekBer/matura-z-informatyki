def get_data():
   with open("./data/uzytkownicy.txt", "r") as f:
      content = f.read().strip().split("\n")
      content = content[1:]
      data = [content[i].split("\t") for i in range(len(content))]
      return data

def main():
   data = get_data()
   dict = {}
   for i in range(len(data)):
      if data[i][1] in dict:
         if(data[i][3] == "tak" and dict[data[i][1]] == "nie" ):
            dict[data[i][1]] = "tak"
      else:
         dict[data[i][1]] = data[i][3]

   counter = 0
   for i in dict:
      if(dict[i] == "nie"):
         counter += 1
   print(counter)


main()