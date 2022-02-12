#subtitle
print ("This project is for draw a triangle with start a.")

#input
triangle_char = input('Enter a character:\n')
triangle_height = int(input('Enter triangle height:\n'))
print('')

#the operation & output
for i in range (len(triangle_char)):
    for j in range (triangle_height):
        print((triangle_char) * triangle_height )
        triangle_height -= 1