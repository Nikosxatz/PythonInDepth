import math
for a in range(-10,11):
    for b in range(-10,11):		
        if a==0 or b==0:
            continue 
        d=b*b-4*a*3
        if d>=0:
            r1=(-b+math.sqrt(d))/(2*a)
            r2=(-b-math.sqrt(d))/(2*a)
            print('a={} b={} r1={}  r2={}'.format(a,b,r1,r2))
        else:
            print('a={} b={} δεν έχει πραγματικές ρίζες'.format(a,b))


        











    
