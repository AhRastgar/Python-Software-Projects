#subtitle
print ("This project is for found prime number.")

#input
x = int (input ("Enter a number for check "))

#the operatin
b = int (0)
y = int ()

for i in range (2, x):
    if x % i == 0:
        y = int (b + 1)

#output
if y == 0:
    print ("This is a prime number.")
else:
    print ("This is not a prime number.")