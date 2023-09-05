etos=int(input('Δώσε έτος:'))
if etos%4==0:
    if etos%100==0:
        if etos%400==0:
            print('Δίσεκτο')
        else:
            print('Κανονικό')
    else:
        print('Δίσεκτο')
else:
    print('Κανονικό')








