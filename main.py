triangle_char = input('Enter a character:\n')
triangle_height = int(input('Enter triangle height:\n'))
counter = 1

print()

for count in range(triangle_height):
  char = triangle_char + ' '
  print(char * counter)
  counter += 1
