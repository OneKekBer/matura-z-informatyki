def get_data():
    with open("./data.txt", "r") as f:
        content = f.read().strip().split("\n")
        data = [content[i].split(' ') for i in range(len(content))]
    return data

def main():
   data = get_data()
   counter = 0

   for arr in data:
      if(arr[0] in arr[1]):
         counter += 1
      
   print(counter)
main()