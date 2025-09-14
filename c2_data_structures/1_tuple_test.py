d = {'A':10, 'B':1, 'C':22}
t = sorted(d.items())
for k, v in t:
    print(k, v)
print('__________________')
e = {'a':10, 'b':1, 'c':22}
f = sorted(e.items())
# The reverse=True is for sorting from greatest to least rather than the normal vice-versa
for k, v in sorted(e.items(), reverse=True):
    print(k, v)

('A') > ('C')

c = {'a':10, 'b':1, 'c':22}
tmp = list()
print(c.items())
for k, v in c.items() :
    tmp.append( (v, k) )
print(tmp)

tmp = sorted(tmp, reverse=True)
print(tmp)
