def get_data():
   with open('./../data/instrukcje.txt', "r") as f:
      content = f.read().strip()
      data = content.split("\t")[0].split("\n")
      
      return data

def get_next_letter(n):
   alfa = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
   for i in range(len(alfa)):
      if n == alfa[len(alfa)-1]:
         return alfa[0]
      if alfa[i] == n:
         return alfa[i+1]

def main():
   data = get_data()
   string = ""
   for i in range(len(data)):
      line = data[i].split(" ")
      comand = line[0]

      if(comand == "DOPISZ"):
         string += line[1]
      elif(comand == "ZMIEN"):
         string = string[:len(string) - 1] + line[1]
      elif(comand == "USUN" and len(string) > 0):
         string = string[:len(string) - 1]
      elif(comand == "PRZESUN"):
         for i in range(len(string)):
            if(string[i] == line[1]):
               string.replace(string[i], get_next_letter(string[i]))

   print(len(string))
main()

#zaebis