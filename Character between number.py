#subtitle
from ctypes.wintypes import CHAR
from email import charset


print ("This project is for add character between numbers.")

#input
x = int (input ("Enter a number "))
char = input ("Enter a character for add between numbers")

#variables
num = x
stash = 0
rev = 0
stash2 = 0
num2 = num

#the operation
for i in range (num % 100):
    stash = int (x % 10)
    
    if stash % 10 == 0:
        break

    x = x / 10
    rev = int (rev * 10 + stash)
    print (rev)

for j in range (num % 100):
    stash2 = int (num2 % 10)
    
    if stash2 % 10 == 0:
        break

    num2 = num2 / 10
    print (stash2, char)