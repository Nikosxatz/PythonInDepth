a=65
b=0.12345678
c='Python'
d=123456789
print('Η {:10} σε βάθος'.format(c))
print('Η {:^10} σε βάθος'.format(c))
print('Η {:>10} σε βάθος'.format(c))
print('a={:+}'.format(a))
print('a={:c}'.format(a))
print('d={:,}'.format(d))
print('d={:b}'.format(d))
print('d={:X}'.format(d))
print('b={:e}'.format(b))
print('b={:%}'.format(b))
print('{1:n}#{2:_}#{0:o}'.format(a,b,d))


