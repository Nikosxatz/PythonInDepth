def fx(x):
    return x**4-10*x**2+2

# Κυρίως πρόγραμμα
i=0
while i<=1:
    print('x={:3.1f} fx={:6.3f}'.format(i,fx(i)))
    i=i+0.05
