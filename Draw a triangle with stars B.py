#subtitle
print ("This project is for draw a triangle with stars B.")

#input
x = int (input ("Enter a number for draw a triangle "))

#the operation & output
for i in range (x + 1): 
    d = x - i 
    e = " " * d + '*' * i 
    print (e)