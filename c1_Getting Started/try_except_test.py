x = input('Enter a positive number: ')
try:
    x = int(x)
except:
    x = 0

if x > 0:
    print('Good Job!')
elif x < 0:
    print('Not a positive number, please try again.')
else:
    print('Not a number or 0.')
