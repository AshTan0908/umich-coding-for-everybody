str = 'Aeroplanes are fast!'

# Find the length of string
print(len(str))

# Print all letters in string
for letter in str:
    print(letter)

index = -1
for letter in str:
    index = index + 1
    print(index, letter)

#Slicing the string
print(str[2])
print(str[0])
print(str[0:11])
print(str[10:])
print(str[:])

# Finding last index
print(str[len(str)-1])

# Finding middle index
x = int(len(str)/2)
print(str[x])
