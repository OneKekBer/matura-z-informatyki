def get_languages():
   with open("./data/uzytkownicy.txt", "r") as f:
      content = f.read().strip().split("\n")
      data = [content[i].split("\t") for i in range(len(content))]

      languages = [i[0] + "\n"+ i[1] for i in data]

      languages = [lang.split("\n") for lang in languages]

      return languages[1:]

def get_continents():
   with open("./data/panstwa.txt", "r") as f:
      content = f.read().strip().split("\n")
      continents = [line.split("\t") for line in content]
      dict = {}

      for line in continents:
         if(line[0] == "Panstwo"):
            continue
         dict[line[0]] = line[1]
      #Country:continent
      return dict  # Assuming the first row is a header and should be skipped


def print_answ(dict):
   with open("./5.3.txt", "w") as f:
      for key in dict:
         if(len(dict[key]) >= 4):
            f.write(f"{key} {dict[key]}\n")

def main():
   dict_continents = get_continents()
   langs = get_languages()


   answ_dict = {}
   for line in langs:
      language = line[1]
      country = line[0]
      continent = dict_continents[country]
      
      if(language in answ_dict):
         if(continent in answ_dict[language]):
            continue
         else:
            answ_dict[language].append(continent)  
         continue

      answ_dict[language] = [continent]
      

   print_answ(answ_dict)


main()