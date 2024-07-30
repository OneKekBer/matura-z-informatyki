def get_languages():
   with open("./data/uzytkownicy.txt", "r") as f:
      content = f.read().strip().split("\n")
      data = [content[i].split("\t") for i in range(len(content))]

      languages = [i[0] + "\n"+ i[1] + "\n" + i[2] for i in data]

      languages = [lang.split("\n") for lang in languages]

      return languages[1:]

def get_families():
   with open('./data/jezyki.txt', "r") as f:
      content = f.read().strip().split("\n")
      content = content[1:]
      data = [content[i].split("\t") for i in range(len(content))]

      dict = {}
      for fam in data:
         dict[fam[0]] = fam[1]

      return dict



def get_continents():
   with open("./data/panstwa.txt", "r") as f:
      content = f.read().strip().split("\n")
      continents = [line.split("\t") for line in content]
      dict = {}

      for line in continents:
         if(line[0] == "Panstwo"):
            continue
         dict[line[0]] = [line[1], line[2]]

      #Country:continent
      return dict  # Assuming the first row is a header and should be skipped

def print_answ(dict):
   with open("./5.4.txt", "w") as f:
      for key in dict:
         f.write(f"{key} {dict[key][2]} {dict[key][3]}\n")

def get_raw_lang_continent_dict(langs, dict_continents):
    answ_dict = {}
    for line in langs:
        country = line[0]
        language = line[1]
        ludzie = float(line[2].replace(",", "."))

        # Ensure the country exists in dict_continents and get the continent
        if country in dict_continents:
            continent = dict_continents[country][0]

            if continent in ["Ameryka Polnocna", "Ameryka Poludniowa"]:
                # Initialize if the language is not already in answ_dict
                if language not in answ_dict:
                    answ_dict[language] = [continent, ludzie]
                else:
                    # Check if the continent is already listed for the language
                    if continent not in answ_dict[language]:
                        answ_dict[language].insert(0, continent)
                    # Add the number of people
                    answ_dict[language][-1] += ludzie

    return answ_dict


def filter_by_two_continents(raw_dict):
   new_dict = {}
   for key in raw_dict:
      if len(raw_dict[key]) == 3:
         new_dict[key] = raw_dict[key]
   return new_dict




def main():
   dict_continents = get_continents()
   langs = get_languages()
   raw_dict= get_raw_lang_continent_dict(langs, dict_continents)
   dict_filtered = filter_by_two_continents(raw_dict)
   
   family_dict = get_families()

   dict_answ = {}
   for key in dict_filtered:
      if(family_dict[key] != "indoeuropejska"):
         dict_answ[key] = dict_filtered[key]
         dict_answ[key].append(family_dict[key])

  
   print_answ(dict_answ)
   
   
main()   

#idk why i dont have 6 countries, mb its my mistake(