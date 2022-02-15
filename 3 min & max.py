#subtitle
print ("This project is for 3 min & max.")

#input
n = int(input("Enter number of elements : "))
 
#variables
a = list(map(int,input("Enter the numbers : ").strip().split()))[:n]

a.sort ()
print ("Minimum = ", a [0], a [1], a[2])

a.sort (reverse = True)
print ("Maximum = ", a [0], a [1], a[2])