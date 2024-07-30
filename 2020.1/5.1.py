def get_data():
   with open('./data/jezyki.txt', "r") as f:
      content = f.read().strip().split("\n")
      content = content[1:]
      data = [content[i].split("\t") for i in range(len(content))]
      return data


def count_families(arr):
    dict_families = {}

    for group in arr:
        family_name = group[1].lower()

        if family_name not in dict_families:
            dict_families[family_name] = 1
        else:
            dict_families[family_name] += 1
    
    return dict(sorted(dict_families.items(), key=lambda item: item[1], reverse=True))


# def sort_dict(dict):
    
def write_answer(dict):
    with open("5.1.txt", "w") as f:
      for i in dict.keys():
         f.write(f"{i} {dict[i]} \n")
      f.close()              

def main():
   data = get_data()
   dict = count_families(data)
   write_answer(dict)
   print(dict)

main()
