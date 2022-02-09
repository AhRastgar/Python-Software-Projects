#subtitle
print ("This project is for prime number.")

#input
x = int (input ("Enter a number for check "))

#the operation
for i in range (2 , x):
    if x % i == 0:
        b = 1

#output
if b == 1:
    print ("yes")
else:
    print ("no")