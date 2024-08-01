def get_users():
   with open('./data/uzytkownicy.txt', "r") as f:
      content = f.read().strip().split("\n")

      data = [content[i].split("\t") for i in range(len(content))]

      return data[1:]

def get_countries():
   with open("./data/panstwa.txt", "r") as f:
      content = f.read().strip().split("\n")

      data = [content[i].split("\t") for i in range(len(content))]

      return data[1:]
   
def print_answ(answ):
   with open("./5.5.txt", "w") as f:
      f.write(f"Panstwo\tProcent\tJezyk\n") 
      for ans in answ:
         f.write(f"{ans[0]}\t{ans[1]}\t{ans[2]}\n") 

def main():
   users = get_users()
   countries = get_countries()
   answ = []
   for country in countries:
      population = float(country[2].replace(",", "."))
      country_name = country[0]

      for user in users:
         user_country = user[0]
         user_language = user[1]
         user_users = float(user[2].replace(",", "."))
         user_isNational = True if user[3] == "tak" else False


         if(country_name == user_country):
            procent = round(user_users * 100 / population, 2)
            if(procent > 30 and not user_isNational):
               data=[user_country, procent , user_language]
               answ.append(data)


   print(answ)
   print_answ(answ)
main()