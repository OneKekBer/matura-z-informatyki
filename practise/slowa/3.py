import itertools 

def get_data():
    with open("./data.txt", "r") as f:
        content = f.read().strip().split("\n")
        data = [content[i].split(' ') for i in range(len(content))]
    return data

def main():
   data = get_data()
   counter = 0
   odp = []
   for arr in data:
      first = arr[0]
      second = arr[1]

      if(len(first) != len(second)):
         continue
      for tuple in itertools.permutations(second):
         
         string = ""
         for letter in tuple:
            string += letter

         if(string in first):
            if([first, second] not in odp):
               odp.append([first, second])
            continue

   print(len(odp))



main()