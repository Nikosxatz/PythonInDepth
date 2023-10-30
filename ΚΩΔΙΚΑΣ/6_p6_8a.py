ls=[(8,7,10,3,5),(6,5.5,2,3),(7,9.5,8,6),(5,7)]
for i in ls:
    sum=0
    cnt=0
    for j in i:
        sum+=j
        cnt+=1
    print('MO=',sum/cnt)



