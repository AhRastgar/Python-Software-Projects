#subtitle
print ("This project is for check reverse number.")

#input
x = int (input ("Enter a number for check reverse "))

#variables
num = x
stash = 0
rev = 0

#the operation
for i in range (x):
    stash = x % 10
    x = x / 10
    rev = rev * 10 + stash

#output
if num == rev:
    print ("This number is a symmetrical number.")
else:
    print ("This number isn't a symmetrical number.")