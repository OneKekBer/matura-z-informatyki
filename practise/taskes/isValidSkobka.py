def isValidSkobka(string):
   print(string)
   stack = []
   for i in range(len(string)):
      if(string[i] == "("):
         stack.append(string[i])
      else:
         if(len(stack) == 0 or stack.pop() != "("):
            return False
   return True

print(isValidSkobka("((()))"))