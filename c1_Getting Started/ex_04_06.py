def computepay(h,r):
    if h <= 40:
        pay = h*r
    else:
        pay = (40*r)+(1.5*(h-40)*r)
    return pay

hrs = input('Enter Hours: ')
h = float(hrs)

rate = input('Enter Rate per Hour: ')
r = float(rate)

p = computepay(h,r)
print('Pay',p)
