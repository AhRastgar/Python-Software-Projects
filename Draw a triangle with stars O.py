#subtitle
print ("This project is for draw a triangle with stars O.")

#input
x = int (input ("Enter a number for draw a triangle "))

#the operation & output
for i in range (1, x + 1): 
    for j in range (1, x + 1):
        if j == x or i == 1 or i == j:
            print ("*", end=" ")
        else:
            print (" ", end=" ")
    print ()