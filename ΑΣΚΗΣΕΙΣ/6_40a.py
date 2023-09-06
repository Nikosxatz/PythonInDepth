import math
t=(-234,-6,56,-6789,4,567,-34,0,67)
mn=math.inf
mx=-mn
for i in t:
    if i>mx: 
        mx=i
    elif i<mn:
        mn=i
print(mx,mn)

















