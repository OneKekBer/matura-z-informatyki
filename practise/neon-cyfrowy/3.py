def get_data():
    with open("./przyklad.txt", "r") as f:
        content = f.read().strip().split("\n")
    return content


def get_next_alfabet_letter(letter):
   alfabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
   letter.upper() 
   for i in range(0, len(alfabet)):
      if(letter == alfabet[i]):
         if(i == len(alfabet) - 1):
            return "A"
         return alfabet[i+1]

def main():
   data = get_data()
   max_length = 0
   max_instruction = ""
   arr = []
   l = 0
   for r in range(len(data)):
      item = data[r]
      instruction = item.split(" ")[0]

      if(len(arr) == 0):
         arr.append(instruction)
         continue

      if(instruction == arr[-1]):
         arr.append(instruction)
         continue

      if(instruction != arr[-1]):
         if(len(arr) > max_length):
            max_instruction = arr[0]
            max_length = len(arr)
         arr = [instruction]
         
   print(max_length, max_instruction)

main()   