# Creating a list
family = [ 'Aashutosh', 'Akzhat', 'Aarti', 'Abhishek']

# Overwriting values in the list with new ones
# Note: Lists in Python follow index way of counting i.e. starts with 0
family[1] = 'Akshat'
family[2] = 'Mumma'
family[3] = 'Daddy'

# Printing the number of family members in family
# Note: Python does not try to decode variables
print('Our family strength is', len(family))

# Greeting all family members
for member in family:
    print('Hello', member)

# Printing the range (Current Status: Fail)
# Reason: Code written by Charles does not produce identical output here
#print(range(4))
#print(range(len(family)))

# Redoing range
x=range(4)
print(list(x))
#y = list(range(len(family)))
print(x)
#print(y)
