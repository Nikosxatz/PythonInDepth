with open('therm.txt','r',encoding='utf-8') as f:
    results=[]
    for line in f:
        sum=0
        s=line.split(',')
        for i in range(1,4):
            sum=sum+float(s[i])
            mo=sum/3
        results.append((mo,s[0]))
        
results.sort(reverse=True)
for p in results:
    print(p[1],'{:4.1f}'.format(p[0]))
print('================')
