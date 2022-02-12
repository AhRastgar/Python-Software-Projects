#subtitle
print ("This project is for draw a triangle with stars A.")

#input
triangle_char = input('Enter a character: ')
triangle_height = int(input('Enter triangle height: '))
print('')

#the operation & output
j = 0

while j <= triangle_height :
    print (triangle_char * j)
    j += 1