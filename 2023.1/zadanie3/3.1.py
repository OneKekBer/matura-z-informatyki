import random
import math
#1
M = 7
a = 2
x = 5

b = ( a ** x ) % M

print(b)

#2
M = 11
a = 3
x = 3

b = ( a ** x ) % M

print(b)

#3

M = 31
a = 5
b = 25


print( math.floor(math.log(M + b, a)) )


#4
M = 59
a = 2
b = 5


print( math.log(M + b, a) )

#5

M = 80
a = 9
x = 2

b = ( a ** x ) % M

print(b)