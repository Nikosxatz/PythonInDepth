import math
NA=math.nan
taxitita=[3.5,NA,5.8,6.0,NA,3.2,2,3.0,NA,4.2]
s=0
pl=0
min=math.inf
max=-math.inf
for t in taxitita:
    if t==t:
        s=s+t
        pl+=1
        if t>max:
            max=t
        elif t<min:
            min=t
mo=s/pl
print('Μέση ταχύτητα:',mo,' Μέγιστη:',max,' Ελάχιστη:',min)


