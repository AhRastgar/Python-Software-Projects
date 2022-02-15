#subtitle
from array import array


print ("This project is for write a numbers on ascending & descending.")

#input
n = int(input("Enter number of elements : "))
 
#variables
a = list(map(int,input("Enter the numbers : ").strip().split()))[:n]

#the operation & output
a.sort ()
print ("Ascending = ", a)

a.sort (reverse = True)
print ("Descending = ", a)