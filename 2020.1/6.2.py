def get_data():
   with open("./data/statek.txt", "r") as f:
      content = f.read().strip().split("\n")[1:]

      data = [content[i].split("\t") for i in range(len(content))]

      return data
   
def print_answ(answ):
   print(answ)
   with open("./6.1.txt", "w") as f:
      f.write(f"Towar\tTonny\n") 
      
      f.write(f"{answ[0]}\t{answ[1][1]}\n") 
      f.close()


def main():
   data = get_data()
   dict_answ = {}

   for i in range(len(data)):
      date = data[i][0]
      country = data[i][1]
      towar = data[i][2]
      ladunek = data[i][3]
      ton = int(data[i][4])
      price = data[i][5]

      year = date.split("-")[0]
      month = date.split("-")[1]
      day = date.split("-")[2]

            

      print(day)
      
main()