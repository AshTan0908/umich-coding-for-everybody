# Enter first number
num1 = input('Enter a number: ')
# If input is not a real number
try:
    a = float(num1)
except:
    print('Entry is not a number.')

# Enter operator
oper = input('Enter sign for operator(add(+),sub(-),multp(*) & div(/): ')

# Enter second number
num2 = input('Enter another number: ')
# If input is not a real number
try:
    b = float(num2)
except:
    print('Entry is not a number.')

# The calculation
if oper == '+':
    print(a,'+',b,'=',a + b)
elif oper == '-':
  print(a,'-',b,'=',a - b)
elif oper == '*':
  print(a,'x',b,'=',a * b)
elif oper == '/':
    if a<b:
        print('Divisor',a, 'is greater than dividend',b)
        print(a,'/',b,'=',a / b)
    else:
        print(a,'/',b,'=',int(a / b),'& remainder is',float(a%b),'.')
        print('OR')
        print(a,'/',b,'=',a / b)
else:
  print('No or wrong operator given.')

# Done
print('Done!')
