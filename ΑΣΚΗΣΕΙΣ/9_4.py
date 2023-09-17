import random
a=[]
s=0
c=0
for i in range(100):
    a.append(random.randint(1000,2000))
for i in a:
	if i%13==0:
		s=s+i
		c=c+1
print(s)


    



