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

   for line in data:
      date = line[0]
      country = line[1]
      towar = line[2]
      ladunek = line[3]
      ton = int(line[4])
      price = line[5]

      if(ladunek == "W"):
         continue
      
      if(towar in dict_answ):
         dict_answ[towar][0] += 1
         dict_answ[towar][1] += ton
      else:
         dict_answ[towar] = [1, ton]

      new_dict = dict(sorted(dict_answ.items(), key=lambda item: item[1], reverse=True))      

   print_answ(list(new_dict.items())[0])

      

main()