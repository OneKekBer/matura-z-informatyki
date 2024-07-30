def get_data():
   with open("./../data/pi.txt", "r") as f:
      content = f.read().strip()
      data = content.split('\n')

      f.close()   
      # print(data)
      return [int(i) for i in data]

def is_group_correct(group):
   # print(group)
   isGroupCorrect = False

   #[2, 5, 4,3,2,1]
   if((group[0] < group[1]) and (group[2] > group[3] and group[3] >  group[4] and group[4] >  group[5])): # первый вар 2-4 rosnaco - malejacy
      isGroupCorrect = True
   # #[5, 2, 1,2,3,4]
   # if((group[0] > group[1]) and (group[2] < group[3] and group[3] <  group[4] and group[4] <  group[5])): # второй вар 2-4 malejaco - rosnasny
   #    isGroupCorrect = True

   if((group[0] < group[1] and group[1] < group[2]) and (group[3] > group[4] and group[4] > group[5])): # первый вар 3-3 rosnaco - malejacy
      isGroupCorrect = True
      
   # if((group[0] > group[1] and group[1] > group[2]) and (group[3] < group[4] and group[4] < group[5])): # первый вар 3-3 malejaco - malejacy
   #    isGroupCorrect = True

   if((group[0] < group[1] and group[1] < group[2] and group[2] < group[3]) and (group[4] > group[5])): # первый вар 4-2 rosnaco - malejacy
      isGroupCorrect = True

   # if((group[0] > group[1] and group[1] > group[2] and group[2] > group[3]) and (group[4] < group[5])): # первый вар 4-2 malejaco - malejacy
   #    isGroupCorrect = True

   if(isGroupCorrect):
      # print(group)
      return group
   else:
      return None;

#[0, 8, 9, 9, 8, 6]
      
def main():
   data = get_data()
   correct_groups = []

   while data:
      group = data[:6]
      data = data[1:] 
      if(len(group) != 6):
         break;
      
      if(is_group_correct(group) == None):
         continue
      else:
         correct_groups.append(is_group_correct(group))


      

   print(len(correct_groups))


main()