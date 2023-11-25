def disekto(e):
    if (e%4==0 and e%100!=0) or e%400==0:
        return True
    else:
        return False

# Κυρίως πρόγραμμα
apo=int(input('Δώσε 1ο έτος:'))
eos=int(input('Δώσε 2ο έτος:'))
print('Δίσεκτα έτη από το {} μέχρι το {}'.format(apo,eos))
print('='*40)
for i in range(apo,eos+1):
    if disekto(i):
        print(i)

