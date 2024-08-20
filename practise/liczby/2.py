def get_data():
    with open("./data.txt", "r") as f:
        content = f.read().strip().split("\n")
    return content

def eight_to_number(number):
   string = str(number)
   string = string[::-1]

   answer = 0
   for i in range(len(string)):
      digit = int(string[i])
      answer += (8 ** (i)) * digit
   return str(answer) 



def main():
   data = get_data()
   counter = 0
   for line in data:
      true_number = eight_to_number(line)
      if(true_number[0] == true_number[-1]): counter += 1 
   print(counter)
      
       

main()